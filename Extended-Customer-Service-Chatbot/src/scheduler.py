# This File Is Created For Automatically Updating The Data Of The Database 

# Importing Library
from apscheduler.schedulers.background import BackgroundScheduler
from lang_chain_helper import create_vector_db


def start_scheduler():
    scheduler = BackgroundScheduler()
    
    # Run Every 6 Hours (You Can Change It)
    scheduler.add_job(create_vector_db,"interval", hours=6)


    # It Is Like Command To Start The scheduler
    scheduler.start()
    print("Scheduler started. Knowledge will update automatically.")










