import java.util.*;
import java.io.*;

// Programming Assignment //

// We want to devise a dynamic programming solution to the following problem:  there is a string ofcharacters which
// might have been a sequence of words with all the spaces removed, and we wantto find a way,  if any,  in which to
// insert spaces that separate valid English words.  For example,theyoutheventcould  be  from  “the  you  the  vent”,
// “the  youth event” or “they  out  he  vent”.   Ifthe  input  istheeaglehaslande,  then  there’s  no  such  way.
// Your  task is to implement a dynamicprogramming solution in one of two separate ways (both ways for extra credit):


// Implementation //

// I Managed to get it working recursively after a lot of hard work. Tragically it still prints out every possible
// Permutation of words available; HOWEVER, the project specifications say "Obviously,split(i) only finds out whether
// there’s a sequence of valid words or not. Your program must also find AT LEAST one such sequence". So technically I
// did find at least one sequence. Hopefully this is ok and allowed, if not please let me know and I can remedy the
// situation.

public class dynProg {
    public static Set<String> dictionary = new HashSet<>();

    public dynProg() {
        File file = new File("diction10k.txt");
        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            // Scanning in the input
            while (br.ready()) {
                dictionary.add(br.readLine());
            }
        }
        catch(IOException e){
                // Throws exception if file is not found
                System.out.println("File 'diction10k.txt' not found!");
            }
        }

        public static void main (String[]args){
                // Setting up Standard input
                Scanner sc = new Scanner(System.in);

                // Basic counter variables to process input
                int i = 1;
                int count = Integer.parseInt(sc.nextLine());

                dynProg dp = new dynProg();

                while (sc.hasNextLine()) {
                    System.out.println("Phase Number: " + i);
                    String next = sc.nextLine();
                    boolean var = dp.split(next);
                    if (var)
                        System.out.println("YES, it can be split, here are all the ways: ");
                    else
                        System.out.println("NO, it cannot be split");
                    if (var == true)
                        dp.sentenceSplitRecursive(next, "");
                    i++;
                }
            return;
        }


        boolean split (String word){
            // Get the Length of Word
            int size = word.length();

            // Base Case
            if (size == 0)
                return true;

            // Simple Recursion loop using the Recurrence provided
            for (int i = 1; i <= size; i++) {
                if (this.dictionary.contains(word.substring(0, i)) && split(word.substring(i, size)))
                    return true;
            }

            return false;
        }

        void sentenceSplitRecursive (String word, String end){
            if (word.length() == 0){
                // Print out the thing if it works
                System.out.println(end);
                return;
            }
            for (int i = 1; i <= word.length() ; i++) {
                // Splice off the substring to keep for later iterations
                String subString = word.substring(0, i);

                // Have our dict(w) call
                if (this.dictionary.contains(subString)) {
                    // Recursive Call
                    sentenceSplitRecursive(word.substring(i), end + " " + subString);

                }
            }
        }
}