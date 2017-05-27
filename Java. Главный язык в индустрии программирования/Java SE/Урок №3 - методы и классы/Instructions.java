class Instructions {
	//HowOnPhone(), HowDownloadGame(), HowChangeSpeaker()

	public static void main(String[] args) {
		HowOnPhone();
		HowDownloadGame();
		HowChangeSpeaker();
	}

	private static void HowOnPhone() {
		System.out.println("\nКак включить телефон?");
		System.out.println("1. Нажмите кнопку включения.");
	}

	private static void HowDownloadGame() { 
		System.out.println("\nКак скачать игру?");
		System.out.println("1. Подключите устройство к компьютеру.");
		System.out.println("2. Запустите файл.");
	}

	private static void HowChangeSpeaker() {
		System.out.println("\nКак сменить динамики?");
		System.out.println("1. Разбейте корпус.");
		System.out.println("2. Поменяйте динамик.");
	}
}