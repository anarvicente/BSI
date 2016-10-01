import java.awt.*;

public class Quadrado extends Figura {
	private int lado;
	
	public Quadrado(String id,int lado, int x, int y){
		super(id,x,y);
		this.lado = lado;
	}


	public void desenhe(Graphics2D g2d){
		g2d.setColor(Color.blue);
		g2d.drawRect(getX()-getLado()/2,getY()-getLado()/2,getLado(),getLado());
	}

	public void imp(){
		super.imp();
		System.out.println("Lado = " + this.lado);
	}

	public int getArea(){
		return lado*lado;
	}

	public void setLado(int lado){
		this.lado = lado;
	}
	
	public int getLado(){
		return this.lado;
	}

	public int getX(){
		return super.getX();
	}

	public int getY(){
		return super.getY();
	}

	public void setX(int x){
		super.setX(x);
	}

	public void setY(int y){
		super.setY(y);
	}
}
