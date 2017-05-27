import java.util.*;

class Thread1 implements Runnable {
	
	int sleep_time;
	String name;
	Random r = new Random();
	//Thread1(name), run()

	public Thread1(String name) {
		this.name = name; //this обращаетс€ к глобальной переменной
		sleep_time = r.nextInt(5000);
	}

	public void run() {
		System.out.printf("ѕоток %s спит %d миллисекунд!\n", name, sleep_time);
		try {                   
			Thread.sleep(sleep_time);  
		}catch (Exception e) {}
		System.out.printf("ѕоток %s проснулс€ и закончилс€!\n", name);
	}
}