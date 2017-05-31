package ru.pavetranquil.lesson2;

import java.util.ArrayList;
import java.util.Random;

public class Worker {
	private ArrayList<Integer> list1 = new ArrayList<Integer>();
	private ArrayList<Integer> list2 = new ArrayList<Integer>();
	private Random r = new Random();
	
	private void partOne() {
		try {
			Thread.sleep(1);
		} catch (InterruptedException e) {}
		list1.add(r.nextInt(100));
	}
	
	private void partTwo() {
		try {
			Thread.sleep(1);
		} catch (InterruptedException e) {}
		list2.add(r.nextInt(100));
	}
	
	private void proceed() {
		for(int i = 0; i<2000; i++){
			partOne();
			partTwo();
		}
	}
	
	public synchronized void start() {
		System.out.println("Начинаем...");
		long startTime = System.currentTimeMillis();
		Thread t1 = new Thread(new Runnable() {

			public void run() {
				proceed();
			}
		});
		Thread t2 = new Thread(new Runnable() {

			public void run() {
				proceed();
			}
		});
		t1.start();
		t2.start();
		
		try {
			t1.join();
			t2.join();
		} catch (InterruptedException e) {}
		long endTime = System.currentTimeMillis();
		System.out.println("Потраченное время: " + (endTime - startTime) + "\n"
				+ "Лист 1: " + list1.size() + "\n"
				+ "Лист 2: " + list2.size());
	}
}
