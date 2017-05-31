package ru.pavetranquil.lesson1;

public class Worker implements Runnable {
	//run()

	public void run() {
		for (int i = 0; i < 2000; i++){
			Code.increaseNumber();
		}

	}

}
