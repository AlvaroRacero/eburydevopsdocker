## COMPLETE NEXT BASH SCRIPT WHERE DEPENDING VALUE OF $ENV START DEVELOPMENT SERVER, PRODUCTION (USING USER CREATED ON DOCKERFILE, SETTING PRODUCTION PORT,
#     AND VISIBILITY), OR TEST MODE


#!/bin/bash
set -e

if [ "$ENV" = 'PROD' ]; then
  echo "Running Production Server"
  exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/ebury.py \
             --callable app --stats 0.0.0.0:9191 --uid $user --gid $group

elif [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server"
  exec python /app/ebury.py 

elif [ "$ENV" = 'TEST' ]; then
  echo "Running Test mode"
  exec python /app/tests.py

else
  echo "Call with correct params"
fi
