from redis_om import get_redis_connection

redis_client = get_redis_connection(
    host="localhost",
    port=6379,
    password="sOmE_sEcUrE_pAsS"
)