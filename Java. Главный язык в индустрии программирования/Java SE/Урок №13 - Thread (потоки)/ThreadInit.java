import java.util.*;

class Thread1 implements Runnable {
	
	int sleep_time;
	String name;
	Random r = new Random();
	//Thread1(name), run()

	public Thread1(String name) {
		this.name = name; //this ���������� � ���������� ����������
		sleep_time = r.nextInt(5000);
	}

	public void run() {
		System.out.printf("����� %s ���� %d �����������!\n", name, sleep_time);
		try {                   
			Thread.sleep(sleep_time);  
		}catch (Exception e) {}
		System.out.printf("����� %s ��������� � ����������!\n", name);
	}
}