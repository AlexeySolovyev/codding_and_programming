class Arrays {
	//PrintElementsOfArray(), NewEmptyArray()

	public static void main(String[] args) {
		NewEmptyArray();
	}

	private static void PrintElementsOfArray() {
		int[] m = {2, 0, 1, 7};

		for (int i = 0; i<4; i++) {
			System.out.println(m[i]);
		}
	}

	private static void NewEmptyArray() {
		int[] m = new int[4];

		for (int i = 0; i<4; i++) {
			m[i] = -i;
			System.out.println(m[i]);
		}
	}
}