
/*


*/
import java.util.*; 
import java.io.*;

class Main {  
  public static String LongestWord(String sen) { 
  
    String arr[] =sen.split(" ");
    
    String lon="";
    int log=0;
    
    for (int i=0;i<arr.length;i++)
    {
        int tem=arr[i].length();
        
        if(tem>log)
        {
            
            log=tem;
            lon=arr[i];
        }
        
    }
    
    
       
    return lon;
    
  } 
  
  public static void main (String[] args) {  
    // keep this function call here     
    Scanner s = new Scanner(System.in);
    System.out.print(LongestWord(s.nextLine())); 
  }   
  
}