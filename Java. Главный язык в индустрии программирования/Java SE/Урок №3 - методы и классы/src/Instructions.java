class Instructions {
	//HowOnPhone(), HowDownloadGame(), HowChangeSpeaker()

	public static void main(String[] args) {
		HowOnPhone();
		HowDownloadGame();
		HowChangeSpeaker();
	}

	private static void HowOnPhone() {
		System.out.println("\n��� �������� �������?");
		System.out.println("1. ������� ������ ���������.");
	}

	private static void HowDownloadGame() { 
		System.out.println("\n��� ������� ����?");
		System.out.println("1. ���������� ���������� � ����������.");
		System.out.println("2. ��������� ����.");
	}

	private static void HowChangeSpeaker() {
		System.out.println("\n��� ������� ��������?");
		System.out.println("1. �������� ������.");
		System.out.println("2. ��������� �������.");
	}
}