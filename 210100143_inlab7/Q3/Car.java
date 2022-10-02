package Q3 ;

/*
 * TODO: Create class Car along with proper methods and inheritance as required
 */

class Car extends Vehicle
{
    public Car(String regNo,String manufacturer,String owner)
    {
        super(regNo, manufacturer, owner);
    }

    @Override public void checkPollutionStatus()
    {
        if(CO2<=15 && CO<=0.5 && HC<=750)
        {
            pollutionStatus = "PASS";
        }
        else
        {
            pollutionStatus = "FAIL";
        }
    }
}