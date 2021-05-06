package application;
	
import java.io.IOException;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


public class Main4 extends Application {

	@Override
	public void start(Stage primaryStage) {
		AnchorPane root;
		try {
			root = (AnchorPane)FXMLLoader.load(getClass().getResource("Main4.fxml"));
			primaryStage.setTitle("Application"); 
			Scene scene = new Scene(root,600,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			
			Button btn = (Button) scene.lookup("#btn");
			TextField tf1  = (TextField) scene.lookup("#tf1");
			TextField tf2  = (TextField) scene.lookup("#tf2");
			TextField tf3  = (TextField) scene.lookup("#tf3");
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					int num1 = Integer.valueOf(tf1.getText());
					int num2 = Integer.valueOf(tf2.getText());
					int sum=0;
					for(int i = num1; i<num2+1; i++) {
						sum += i;
					}
					tf3.setText(sum+"");
				}
			});
			primaryStage.setScene(scene);
			primaryStage.show();
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
	}
	
	public static void main(String[] args) {
		launch(args);
	}
	
}
