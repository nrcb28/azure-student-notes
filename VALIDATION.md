# Validation record / Registro de validación

Checks performed for the common-core and advanced-lab revision:

- Documentation links, language file coverage, source integrations, and Bash syntax: passed.
- Common-core checker: twelve foundation units and twenty certification units in every language, with corresponding lab commands: passed.
- Local behavioural tests: seven passed. They cover lost responses, duplicate prevention, unconfirmed writes, permanent failures, invalid retry budgets, and guards that reject unsuitable lab inputs before cloud commands.
- SQLite simulation: with three allowed attempts, naive processing creates two records and idempotent processing creates one. A permanent failure is not retried and writes nothing. With one allowed attempt, a write can exist without a confirmed successful response.
- Bicep CLI 0.48.1: the base storage, base network, and new protected-storage templates compile locally.

No Azure deployment, Blob restore against Azure, effective-permission check against a real tenant, or measured recovery timing was performed. Local compilation does not establish cloud quota, policy, permissions, regional capacity, pricing, or operational success.

No se ejecutaron despliegues ni restauraciones en Azure, ni consultas de permisos en un tenant real. La compilación local no demuestra cuotas, políticas, permisos, disponibilidad regional, precios o éxito operativo.

Structural parity checks do not certify language quality or establish complete translation of older supplementary notes. See [STUDY-PARITY.md](STUDY-PARITY.md).
