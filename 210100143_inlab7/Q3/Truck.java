package Q3 ;

/*
 * TODO: Create class Truck along with proper methods and inheritance as required
 */
class Truck extends Vehicle
{
    public Truck(String regNo,String manufacturer,String owner)
    {
        super(regNo, manufacturer, owner);
    }

    @Override public void checkPollutionStatus()
    {
        if(CO2<=25 && CO<=0.8 && HC<=1000)
        {
            pollutionStatus = "PASS";
        }
        else
        {
            pollutionStatus = "FAIL";
        }
    }
}