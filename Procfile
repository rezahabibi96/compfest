release: orator migrate -p './apps/migrations' -c './apps/migrations/__init__.py' -f
web: uvicorn main:app --host 0.0.0.0 --port $PORT