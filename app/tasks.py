#Placeholder for now.
from app import app, database

def dailyTasks():
    db = database.MyDatabase()
    sql="""
    INSERT INTO kwhTotalsDay(kwhtotal) VALUES((
    SELECT kwhtotal FROM kwhTotals 
    ORDER BY ts DESC LIMIT 1));
    """
    db.modifyq(sql)

    #Remove old useless data
    db = database.MyDatabase()
    sql="""
    DELETE FROM kwhTotals
    WHERE ts < NOW() - INTERVAL '7 days';
    """
    db.modifyq(sql)
    app.logger.info("Daily task complete")