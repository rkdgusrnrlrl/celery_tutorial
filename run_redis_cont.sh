
mkdir -p data

if [[ "$(docker ps -a | grep "some-redis" 2> /dev/null)" != "" ]]; then
  docker rm -f "some-redis"
  echo "삭제 됨"
fi

docker run --name some-redis -d -v data:/data -p 6379:6379 redis redis-server --appendonly yes