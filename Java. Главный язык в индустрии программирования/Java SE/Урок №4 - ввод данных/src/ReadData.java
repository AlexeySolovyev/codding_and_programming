class ReadData {
	//count()

	public static void main(String[] args) {
		Reader r = new Reader();
		r.Scan();

		r.i = count(r.i);
		r.k = count(r.k);

		System.out.println("\n������ ������ ���� ����� = " + r.i);
		System.out.println("\n������ ������ ���� ����� = " + r.k);
	}

	private static int count(int x) {
		x = x * 3;
		return x;
	}
}