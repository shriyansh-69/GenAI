# This File Is Created For Automatically Updating The Data Of The Database 

# Importing Library
from apscheduler.schedulers.background import BackgroundScheduler
from lang_chain_helper import create_vector_db

scheduler = BackgroundScheduler()


def start_scheduler():
    if not scheduler.running:
        scheduler.add_job(create_vector_db,"interval", minutes = 30)
        scheduler.start()
        print("Scheduler Started. Knowledge will update automatically. ")
    
    










