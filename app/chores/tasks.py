from app import app
from app.chores import queries

tax = app.config['TAX']
tz = app.config['TZ']
cost = float(app.config['COST'])


# Misc Tasks

def tskQryToList(qry):
    return list(map(tskQryToList, qry)) \
        if isinstance(qry, (list, tuple)) \
        else qry


def tskGetBills(limit):
    Bills = queries.qryGetBills(limit)
    for inner_list in Bills:
        inner_list[1] = round((inner_list[1] * float(cost)) * tax, 2)
    return Bills


def tskGetBillingData(id):
    billDateInfo = queries.qryGetBillDate(id)
    billDate = billDateInfo[0][0]
    billDateName = billDateInfo[0][1]

    avgKwhRaw = queries.qryBillAvgKwh(billDate)[0][0]
    avgKwh = round(avgKwhRaw, 3)

    kwhHiLo = queries.qryBillKwhHiLo(billDate)

    billKwhTotal = queries.qryBillKwhTotal(id)[0][0]
    billNoTaxCost = round(billKwhTotal * float(cost), 2)
    billTax = billNoTaxCost * float(tax)
    billKwhTotalCost = billTax + billNoTaxCost


    billDayKwh = queries.qryBillDayKwh(billDate)

    return (
        avgKwh,
        kwhHiLo,
        billKwhTotalCost,
        billKwhTotal,
        billDateName,
        billDayKwh,
        billTax,
        billNoTaxCost
    )


def tskCalculateCost():
    kwhDayTotal = queries.qryDayKwhTotal()[0][0]
    kwhDayCost = round(kwhDayTotal * cost, 2)

    kwh7dTotal = queries.qryKwh7dTotal()[0][0]
    if kwh7dTotal is None:
        kwh7dTotal = 0
    kwh7dCost = round(kwh7dTotal * cost, 2)

    kwhPrevMnTotal = queries.qryKwhPrevMn()[0][0]
    kwhPrevMnCost = round(kwhPrevMnTotal * cost, 2)

    kwhPeakDayMn = queries.qryPeakKwhDayMn()[0][0]
    kwhPeakDayMnCost = round(kwhPeakDayMn * cost, 2)

    kwhLowDayMn = queries.qryLowKwhDayMn()[0][0]
    kwhLowDayMnCost = round(kwhLowDayMn * cost, 2)

    kwhAvgDayMn = queries.qryAvgKwhDayMn()
    kwhAvgDayMnCost = round(kwhAvgDayMn * cost, 2)

    return(
        kwhDayCost,
        kwh7dCost,
        kwhPrevMnCost,
        kwhPeakDayMnCost,
        kwhLowDayMnCost,
        kwhAvgDayMnCost
    )
