
mkdir -p data

docker run --name some-redis -d -v data:/data -p 6379:6379 redis redis-server --appendonly yes