class fibonacciseries{  
public static void main(String args[])  //
{    
 int n1=0,n2=1,n3,i,count=10;    
 System.out.print(n1+" "+n2);//printing 0 and 1    
    
 for(i=2;i<count;++i)//starting the loop at 2 because 0 and 1 are printed   
 {    
  n3=n1+n2;    
  System.out.print(" "+n3);    
  n1=n2;    
  n2=n3;    //1 converted to 2, 2 converted to 3 so on
 }    
  
}}