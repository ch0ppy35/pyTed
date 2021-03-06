docker login --username "$DOCKER_USER" --password "$DOCKER_PASS"
if [ "$TRAVIS_BRANCH" = "dev" ]; then
  TAG="latest"
else
  TAG="$TRAVIS_BRANCH"
fi
TRAVIS_REPO_SLUG=`echo $TRAVIS_REPO_SLUG | tr '[:upper:]' '[:lower:]'`
docker build -f Dockerfile -t $TRAVIS_REPO_SLUG:$TAG .
docker tag $TRAVIS_REPO_SLUG $DOCKER_REPO
docker push $DOCKER_REPO