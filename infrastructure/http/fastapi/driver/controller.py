from fastapi import APIRouter, Depends, HTTPException

from application.driver.driver_schema import DriverSchema
from application.driver.use_case.get_all_drivers import GetAllDrivers

router = APIRouter(prefix="/driver", tags=["Driver"])


@router.get("/", status_code=200, response_model=list[DriverSchema])
async def get_all_drivers():
    try:

        use_case = GetAllDrivers('abc')
        return await use_case.execute()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/", status_code=201, response_model=DriverSchema)
async def create_driver():
    try:
        use_case = GetAllDrivers('abc')
        return await use_case.execute()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{driver_id}", status_code=200, response_model=DriverSchema)
async def get_calendar():
    try:
        use_case = GetAllDrivers('abc')
        return await use_case.execute()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{driver_id}", status_code=200, response_model=DriverSchema)
async def update_calendar(driver_id: int, driver: DriverSchema):
    try:
        use_case = GetAllDrivers('abc')
        return await use_case.execute()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{driver_id}", status_code=200,
               response_model=DriverSchema)
async def delete_calendar(calendar_id: int):
    try:
        use_case = GetAllDrivers('abc')
        return await use_case.execute()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
