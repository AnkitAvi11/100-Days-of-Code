class MyArray {
    
    int[] arr;
    int size;
    int top;

    public MyArray () {
        this.arr = new int[5];
        this.size = 5;
        this.top = -1
    }

    public MyArray(int size) {
        this.arr = new int[size];
        this.size = size;
        this.top = -1;
    }

    public void insert(int value) 
    {   
        if(this.top == this.arr.length-1) {
            System.out.println("Array is completely filled");
        }else{
            this.arr[++this.top] = value;
        }
    } 

    public int delete(int sk) 
    {
        int pos = -1;
        for(int i = 0;i<this.arr.length; i++){
            if(arr[i] == sk){
                pos = i;
                break;
            }
        }

        if(pos != -1){
            for(int i = pos;i<arr.length-1;i++){
                this.arr[i] = this.arr[i+1];
            }
            this.top = -1;
            return sk;
        }else{
            return -1;
        }
    }

    public int search(int sk)
    {
        for(int el:this.arr) {
            if (el == sk) {
                return sk;
            }
        }
        return -1;
    }

    public int iterativeBinarySearch(int sk)
    {
        int left = 0, right = arr.length -1;

        while (left <= right) {
            int mid = (left+right) / 2;   
            if (sk < arr[mid] ) {
                right = mid-1;
            }else if (sk >  arr[mid] ) {
                left = mid+1;
            }else if (sk == arr[mid]) {
                return mid+1;
            }
        }

        return -1;
    }

}

//  Driver code for the program
public class ArrayExample {

    public static void main(String[] args) {
        
    }
}