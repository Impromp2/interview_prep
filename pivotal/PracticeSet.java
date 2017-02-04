public class PracticeSet {

	private int[] contents;
	private int count;
	private int capacity = 128; // Default capacity

	public static void main(String[] args) {
		if (args.length > 0) {
			PracticeSet set = new PracticeSet(args);
		} else {
			PracticeSet set = new PracticeSet();
		}
	}

	public PracticeSet() {
		count = 0;
    	contents = new int[capacity];
	}

	public PracticeSet(String[] set) {
		count = set.length;
		contents = new int[capacity];
		addAll(set);
	}

	public boolean isEmpty() {
		if (count == 0 || contents == null) {
			return true;
		} else {
			return false;
		}
	}

	public void addAll(String[] set) {
		System.out.println("Got " + set.length + " items");
	}
}