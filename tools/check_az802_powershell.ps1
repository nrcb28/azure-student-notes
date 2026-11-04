#Requires -Version 7.0

# Parse documentation examples without running the commands they contain.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repositoryRoot = [System.IO.Path]::GetFullPath(
    [System.IO.Path]::Combine($PSScriptRoot, '..')
)
$certificationsRoot = Join-Path $repositoryRoot 'certifications'
$languages = @('en', 'es', 'de', 'fr', 'it', 'ru', 'ja', 'zh')
$fileNames = @('AZ-802.md', 'AZ-802-cases.md', 'AZ-802-workbook.md')
$documents = @(
    Get-ChildItem -LiteralPath $certificationsRoot -Filter 'AZ-802*.md' -File -Recurse |
        Sort-Object FullName
)
$errorCount = 0

foreach ($language in $languages) {
    foreach ($fileName in $fileNames) {
        $expectedPath = Join-Path $certificationsRoot $language $fileName
        if (-not (Test-Path -LiteralPath $expectedPath -PathType Leaf)) {
            [Console]::Error.WriteLine("Missing AZ-802 document: certifications/$language/$fileName")
            $errorCount++
        }
    }
}

$guideCount = @($documents | Where-Object Name -CEQ 'AZ-802.md').Count
if ($documents.Count -ne 24 -or $guideCount -ne 8) {
    [Console]::Error.WriteLine((
        'Expected 24 AZ-802 Markdown files including 8 guides; found {0} files and {1} guides.' -f
        $documents.Count, $guideCount
    ))
    $errorCount++
}
if ($errorCount -gt 0) {
    exit 1
}

function Get-PowerShellSyntaxErrorCount {
    param(
        [AllowEmptyString()][string] $Code,
        [string] $DocumentPath,
        [int] $FirstContentLine,
        [int] $BlockNumber
    )

    if ([string]::IsNullOrWhiteSpace($Code)) {
        [Console]::Error.WriteLine((
            '{0}:{1}: PowerShell block {2} is empty.' -f
            $DocumentPath, $FirstContentLine, $BlockNumber
        ))
        return 1
    }

    $tokens = $null
    $parseErrors = $null
    $null = [System.Management.Automation.Language.Parser]::ParseInput(
        $Code, [ref] $tokens, [ref] $parseErrors
    )
    if ($null -eq $parseErrors) {
        return 0
    }
    foreach ($parseError in $parseErrors) {
        $documentLine = $FirstContentLine + $parseError.Extent.StartLineNumber - 1
        [Console]::Error.WriteLine((
            '{0}:{1}:{2}: PowerShell block {3}: {4} [{5}]' -f
            $DocumentPath, $documentLine, $parseError.Extent.StartColumnNumber,
            $BlockNumber, $parseError.Message, $parseError.ErrorId
        ))
    }
    return @($parseErrors).Count
}

$blockCount = 0
$utf8 = [System.Text.UTF8Encoding]::new($false, $true)
foreach ($document in $documents) {
    $documentPath = [System.IO.Path]::GetRelativePath(
        $repositoryRoot, $document.FullName
    ).Replace('\', '/')
    try {
        # ReadAllLines auto-detects UTF-16/UTF-32 BOMs even with a UTF-8 encoding.
        # Decode bytes directly so the exception fallback enforces UTF-8.
        $content = $utf8.GetString([System.IO.File]::ReadAllBytes($document.FullName))
        if ($content.StartsWith([string][char] 0xFEFF)) {
            $content = $content.Substring(1)
        }
        $lines = @($content -split '\r\n|\n|\r')
    }
    catch {
        [Console]::Error.WriteLine(('{0}: Cannot read UTF-8 document: {1}' -f $documentPath, $_.Exception.Message))
        $errorCount++
        continue
    }

    $insideFence = $false
    $isPowerShell = $false
    $closingPattern = ''
    $openingLine = 0
    $firstContentLine = 0
    $fenceIndent = 0
    $fileBlockCount = 0
    $codeLines = [System.Collections.Generic.List[string]]::new()

    for ($lineIndex = 0; $lineIndex -lt $lines.Count; $lineIndex++) {
        $line = $lines[$lineIndex]
        if (-not $insideFence) {
            if ($line -match '^(?<indent> {0,3})(?<fence>`{3,}|~{3,})(?<info>.*)$') {
                $fence = $Matches['fence']
                $info = $Matches['info'].Trim()
                $fenceIndent = $Matches['indent'].Length
                $insideFence = $true
                $isPowerShell = $info -imatch '^(powershell|pwsh|ps1)(?:\s|$)'
                $closingPattern = '^ {0,3}' + [regex]::Escape($fence.Substring(0, 1)) +
                    '{' + $fence.Length + ',}[ \t]*$'
                $openingLine = $lineIndex + 1
                $firstContentLine = $lineIndex + 2
                $codeLines.Clear()
                if ($isPowerShell) {
                    $fileBlockCount++
                    $blockCount++
                }
            }
            continue
        }

        if ($line -match $closingPattern) {
            if ($isPowerShell) {
                $blockArguments = @{
                    Code = $codeLines -join "`n"
                    DocumentPath = $documentPath
                    FirstContentLine = $firstContentLine
                    BlockNumber = $fileBlockCount
                }
                $errorCount += Get-PowerShellSyntaxErrorCount @blockArguments
            }
            $insideFence = $false
        }
        elseif ($isPowerShell) {
            # CommonMark removes up to the opening fence's space indentation.
            $removedSpaces = 0
            while ($removedSpaces -lt $fenceIndent -and
                $removedSpaces -lt $line.Length -and $line[$removedSpaces] -eq ' ') {
                $removedSpaces++
            }
            $codeLines.Add($line.Substring($removedSpaces))
        }
    }

    if ($insideFence) {
        [Console]::Error.WriteLine((
            '{0}:{1}: Code fence is not closed; syntax coverage is incomplete.' -f
            $documentPath, $openingLine
        ))
        $errorCount++
    }
    if ($document.Name -ceq 'AZ-802.md' -and $fileBlockCount -ne 9) {
        [Console]::Error.WriteLine((
            '{0}: Expected 9 PowerShell blocks; found {1}.' -f
            $documentPath, $fileBlockCount
        ))
        $errorCount++
    }
}

if ($blockCount -eq 0) {
    [Console]::Error.WriteLine('No PowerShell code blocks found in the AZ-802 documents.')
    $errorCount++
}
if ($errorCount -gt 0) {
    [Console]::Error.WriteLine(('AZ-802 PowerShell syntax check failed with {0} error(s).' -f $errorCount))
    exit 1
}

Write-Host (
    'Parsed {0} PowerShell blocks in {1} AZ-802 Markdown files ({2} guides). ' -f
    $blockCount, $documents.Count, $guideCount
)
Write-Host 'Syntax only; no documentation commands were executed or Windows roles validated.'
