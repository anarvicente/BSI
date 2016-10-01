 import java.awt.*;
 import java.awt.event.*;

 public class Example01 extends Frame {
	 /* Frame  a janela grafica onde as figuras serao dispostas */
	  PilhaFigura pf; 
	 /* o vetor de Figuras que servira de container para adicionar as figuras.
	 * 
	 */
	private static final long serialVersionUID = 1L;

/**
    * Um objeto  Example01 � criado. 
    **/
	//   public static void main(String args[]) {
	//     
	//     new Example01();
	//   }

   /**
    * Our Example01 constructor sets the frame's size, adds the
    * visual components, and then makes them visible to the user.
    * It uses an adapter class to deal with the user closing
    * the frame.
    * O construtor de Example01 define o tamanho do frame, adiciona componentes visuais, como o titulo
    * deixa o frame visivel para o usuario.
    **/
   public Example01(PilhaFigura p) {
     //Title our frame.
     super("Pilha de Figuras - A Figura mais interna estah no topo");
     pf = p;

     //Set the size for the frame.
     setSize(700,700);

     //We need to turn on the visibility of our frame
     //by setting the Visible parameter to true.
     setVisible(true);

     //Now, we want to be sure we properly dispose of resources
     //this frame is using when the window is closed.  We use
     //an anonymous inner class adapter for this.
     /* foi criado aqui um adapatador de classe para que a janela responda
      * corretamente  aos eventos de fechamento. Sem este adaptador a janela n�o fechara ao clique 
      * do close window
      */
      addWindowListener(new WindowAdapter()
       {public void windowClosing(WindowEvent e)
          {dispose(); System.exit(0);}
       }
     ); 
  }

   /**
    * The paint method provides the real magic.  Here we
    * cast the Graphics object to Graphics2D to illustrate
    * that we may use the same old graphics capabilities with
    * Graphics2D that we are used to using with Graphics.
    **/
   public void paint(Graphics g) {
      int nf,i=0;
      Figura f;
     //Here is how we used to draw a square with width
     //of 200, height of 200, and starting at x=50, y=50.
      g.setColor(Color.red);
     //g.drawRect(50,500,200,200);
    
     //Let's set the Color to blue and then use the Graphics2D
     //object to draw a rectangle, offset from the square.
     //So far, we've not done anything using Graphics2D that
     //we could not also do using Graphics.  (We are actually
     //using Graphics2D methods inherited from Graphics.)
     Graphics2D g2d = (Graphics2D)g;

     
     nf = pf.getNFiguras();
     for (i=0;i<nf;i++) {
         f = (Figura)pf.desempilhe();
         f.desenhe(g2d);
     }
   }
 }