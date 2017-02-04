import java.util.ArrayList;

public class Set {
    private ArrayList storedArray;

    /*
         *initialize everything in constructor
    */
    Set(){
        this.storedArray = new ArrayList();
    }

    /*
         * check if element is present in the Set Array
    */
    private boolean contains(T elem){
        if(this.storedArray.contains(elem)){
            return true;
        }
        return false;
    }

    /*
         *Add element to the set array
     */
    public void add(T elem) throws Exception{
        if(!contains(elem)){
            this.storedArray.add(elem);
        }else{
            throw new exceptions("DuplicateObjectInsertion");
        }
    }

    /*
         *remove all elements from the set array
    */
    public void clear(){
        this.storedArray = new ArrayList();
    }

    /*
         *Get size of the set array
    */
    public int getSize(){
        return this.storedArray.size();
    }

    /*
         *get first element of the set array
    */
    public T getFirst(){
        return this.storedArray.get(0);
    }

    /*
         *get last element of the set array
    */
    public T getLast(){
        return this.storedArray.get(this.storedArray.size() - 1 );
    }

    /*
         *print the set array
    */
    public void PrintSet(){
        for(T elem : this.storedArray){
            System.out.print(elem.toString() + "\t" );
        }
        System.out.println("");
    }

}