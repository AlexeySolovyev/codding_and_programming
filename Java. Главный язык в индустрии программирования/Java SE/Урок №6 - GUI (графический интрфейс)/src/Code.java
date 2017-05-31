class Code {
	//count()
	
	public static void main(String[] args) {
		Graphic g = new Graphic();
		g.Input();

		g.i = count(g.i);
		g.k = count(g.k);

		g.Show(g.i, g.k);
	}

	private static int count(int x) {
		x = x * 3;
		return x;
	}
}