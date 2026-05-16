from arq.connections import RedisSettings

async def analyser_dce(ctx, fichier_id: int):
    print(f"Analyse du projet {fichier_id} en cours...")

class WorkerSettings:
    redis_settings = RedisSettings()
    functions = [analyser_dce]