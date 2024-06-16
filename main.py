# main.py
from fastapi import FastAPI, HTTPException
from database import database
from model import test_table
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

app = FastAPI()


@app.on_event("startup")
async def startup():
    try:
        await database.connect()
        logging.info("Database connection established successfully")
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        raise e


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



@app.get("/data")
async def read_users():
    query = test_table.select()
    return await database.fetch_all(query)





@app.post("/data")
async def create_form(first_name: str, last_name: str, email: str, country: str, phone: str, languages: str,
                      linkedin: str, experience:str, annual_compensation:str):
    try:
        query = test_table.insert().values(first_name=first_name, last_name=last_name, email=email, country=country,
                                           phone=phone, languages=languages, linkedin=linkedin, experience=experience, annual_compensation=annual_compensation)
        await database.execute(query)
        return {"First Name": first_name, "Last Name": last_name, "email": email, "country": country,
                "Phone Number": phone,
                "Languages": languages, "Linkedin": linkedin, "Experience": experience, "Annual Compensation": annual_compensation}
    except Exception as e:
        error_message = f"Error occurred while inserting data: {str(e)}"
        raise HTTPException(status_code=500, detail=error_message)
