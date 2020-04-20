#!/usr/bin/env bash
docker run -d -p 15672:15672 -p 15671:15671 -p 5672:5672 -p 5671:5671 --hostname yafra --name yaframq rabbitmq:3-management-alpine
docker logs yaframq
source /work/venv/bin/activate
pip install -r requirements.txt
python test-client.py
