public class Example4 {
    int id = 301; // instance variable
    static int fees; // static variable

    void collegeDetails() {
        int rank = 1; // local variable
        System.out.println("AAC College ID: DIT " + id);
        System.out.println("AAC College Rank: " + rank);
    }

    public static void main(String[] args) {
        Example4 st = new Example4();
        fees = 6666;
        System.out.println("Curent Fees: " + fees);
        st.collegeDetails();
    }
}     