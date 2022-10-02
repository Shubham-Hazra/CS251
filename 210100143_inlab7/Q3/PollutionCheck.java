package Q3;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;

public class PollutionCheck {

    public static void main(String [] args) throws Exception {
        /*
         * Implement this function to produce the desired outputs
         */
        HashMap<String, Vehicle> map = new HashMap<>();
        List<String> query_list = new ArrayList<String>();
        File queries = new File(args[2]);
        BufferedReader br2 = new BufferedReader(new FileReader(queries));
        String st2;
        while ((st2 = br2.readLine()) != null)
        {
            Boolean foundinvehicles = false;
            query_list.add(st2);
            File vehicles = new File(args[0]);
            BufferedReader br = new BufferedReader(new FileReader(vehicles));
            String st;
            while ((st = br.readLine()) != null)
            {
                String arr[] = st.split(", ",-1);
                if(st2.equals(arr[0]))
                {
                    Boolean foundinpollution = false;
                    foundinvehicles = true;
                    if(arr[3].equals("Car"))
                    {
                        Vehicle v = new Car(arr[0],arr[1],arr[2]);
                        BufferedReader br1 = new BufferedReader(new FileReader(args[1]));
                        String st1;
                        while ((st1 = br1.readLine()) != null)
                        {
                            String arr1[] = st1.split(", ",-1);
                            if(arr[0].equals(arr1[0]))
                            {
                                foundinpollution = true;
                                v.add_data(Double.valueOf(arr1[1]),Double.valueOf(arr1[2]),Double.valueOf(arr1[3]));
                                v.checkPollutionStatus();
                                System.out.println(v.pollutionStatus);
                            }
                        }
                        map.put(arr[0],v);
                        if(!foundinpollution)
                        {
                            System.out.println("PENDING");
                        }
                        foundinpollution = false;
                    }
                    else if(arr[3].equals("Truck"))
                    {
                        Vehicle v = new Truck(arr[0],arr[1],arr[2]);
                        BufferedReader br1 = new BufferedReader(new FileReader(args[1]));
                        String st1;
                        while ((st1 = br1.readLine()) != null)
                        {
                            String arr1[] = st1.split(", ",-1);
                            if(arr[0].equals(arr1[0]))
                            {
                                foundinpollution = true;
                                v.add_data(Double.valueOf(arr1[1]),Double.valueOf(arr1[2]),Double.valueOf(arr1[3]));
                                v.checkPollutionStatus();
                                System.out.println(v.pollutionStatus);
                            }
                        map.put(arr[0],v);
                    }
                    if(!foundinpollution)
                    {
                        System.out.println("PENDING");
                    }
                    foundinpollution = false;
                    
                }
                }
            }
            if(!foundinvehicles)
            {
                System.out.println("NOT REGISTERED");
            }
        }
        br2.close();
    }
}