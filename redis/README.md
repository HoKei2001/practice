# what is redis?
- Redis is an in-memory data store
- Uses key-value structures
- Traditionally used as a caching layer
- Data stored in RAM (very fast)

# Connect to Redis database
- we lauch the Redis docker image `redis:alpine` at `localhost:6379`

```docker-compose.yaml
  redis:
    image: "redis:alpine"
    command: redis-server --requirepass sOmE_sEcUrE_pAsS
    ports:
      - "6379:6379"
    networks:
      - utilities
    volumes:
      - ./mounts/redis:/data
```

