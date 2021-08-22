from fastapi import FastAPI
import psycopg2
from psycopg2 import sql
import os
import io
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/")
async def root(token: str, dbhost: str, dbname: str ,username: str, passwd: str,table: str,port: str,):
    if token == "XYZ":
        con = psycopg2.connect(dbname=dbname, user=username, password=passwd, host=dbhost, port=port)
        cur = con.cursor()
        save = "{}.csv".format(table)
        store = sql.SQL("""COPY {table} TO STDOUT WITH CSV HEADER""").format(table=sql.Identifier(table),)
        text_stream = io.StringIO()
        cur.copy_expert(store, text_stream)
        con.commit()
        cur.close()
        con.close()
        response = StreamingResponse(iter([text_stream.getvalue()]),
                             media_type="text/csv"
        )
        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
        return response
    else:
        return {"error":"failed"}