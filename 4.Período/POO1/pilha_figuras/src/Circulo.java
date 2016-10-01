
import java.awt.*;
import java.awt.event.*;
import java.lang.Math;

public class Circulo extends Figura {
	private int raio;
	
	public Circulo(String id,int raio, int x, int y){
		super(id,x,y);
		this.raio = raio;
	}

	public void imp(){
		super.imp();
		System.out.println("Raio = " + this.raio);
	}

	public void desenhe(Graphics2D g2d) {
		g2d.setColor(Color.green);
		g2d.drawOval(getX() - getRaio() ,  getY() - getRaio() ,  2*getRaio() ,  2*getRaio());
	}

	public void setRaio(int raio){
		this.raio = raio;
	}

	public int getRaio(){
		return this.raio;
	}

	public void setX(int x){
		super.setX(x);
	}

	public void setY(int y){
		super.setY(y);
	}

	public int getX(){
		return super.getX();
	}

	public int getY(){
		return super.getY();
	}

	public String getId(){
		return super.getId();
	}

	public Double getArea(){
		return Math.PI* Math.pow(this.raio,2);
	}
}
