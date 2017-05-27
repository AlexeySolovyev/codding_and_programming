class MultiArray {
	//EmptyMultiArray(), FullMultiArray() 

	public static void main(String[] args) {
		int[][] m = {{1, 3, 5}, {2, 4, 6}, {0, 1}};
		for (int i = 0; i<3; i++) {
			for (int ii = 0; ii<m[i].length; ii++){
				System.out.print(m[i][ii] + "  ");
			}
			System.out.println();
		}
	}

	private static void EmptyMultiArray() {
		int[][] m = new int[3][3];
	}

	public static void FullMultiArray() {
		int[][] m = {{1, 3, 5}, {2, 4, 6}, {0, 1}};
	}
}