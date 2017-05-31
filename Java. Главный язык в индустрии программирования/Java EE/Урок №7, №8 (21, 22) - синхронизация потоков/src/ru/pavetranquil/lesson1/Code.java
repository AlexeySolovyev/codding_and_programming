package ru.pavetranquil.lesson1;

public class Code {
	private static int number;
	//increaseNumber(num)

	public static void main(String[] args) {
		Thread t1 = new Thread(new Worker());
		Thread t2 = new Thread(new Worker());
		
		t1.start();
		t2.start();
		
		try {
			t1.join();
			t2.join();
		} catch (InterruptedException e) {}
		
		System.out.println(number);
	}
	
	public static synchronized void increaseNumber() { //synchronized - синхронизирует потоки. ставит их в очередь и организует
		number++;
	}

}
