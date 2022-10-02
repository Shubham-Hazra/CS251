package Q3;

/*
 * TODO: Create class Vehicle along with given attributes and methods 
 */

public class Vehicle{
    String regNo;
    String manufacturer;
    String owner;
    double CO2;
    double CO;
    double HC;
    String pollutionStatus;

    public Vehicle(String regNo,String manufacturer,String owner)
    {
        this.regNo = regNo;
        this.manufacturer = manufacturer;
        this.owner= owner;
        pollutionStatus = "PENDING";
    }

    public void add_data(double CO2,double CO,double HC)
    {
        this.CO2 = CO2;
        this.CO = CO;
        this.HC = HC;
    }

    public void checkPollutionStatus()
    {
        return;
    }

    public String toString()
    {
        String s = "Reg No: "+regNo+"\nManufacturer: "+manufacturer+"\nOwner: "+owner+"\nPollution Status: "+pollutionStatus;
        return s;
    }
}