package com.figures.figuresfx;
import com.figures.interfaces.IShape;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.image.WritableImage;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.List;
import java.util.Objects;
import com.figures.storage.Storage;

public class FiguresApp extends Application {


    private WritableImage image;
    private GraphicsContext graphicsContext;


    @Override
    public void start(Stage stage) throws IOException {


        FXMLLoader fxmlLoadermain = new FXMLLoader(FiguresApp.class.getResource("main-view.fxml"));
        FXMLLoader fxmlLoaderaddfigure = new FXMLLoader(FiguresApp.class.getResource("add_figure-view.fxml"));
        FXMLLoader fxmlLoadermovefigure = new FXMLLoader(FiguresApp.class.getResource("move_figure-view.fxml"));
        FXMLLoader fxmlLoaderdeletefigure = new FXMLLoader(FiguresApp.class.getResource("delete_figure-view.fxml"));
        FXMLLoader fxmlLoadercrossfigure = new FXMLLoader(FiguresApp.class.getResource("cross_figure-view.fxml"));
        FXMLLoader fxmlLoadersquarefigure = new FXMLLoader(FiguresApp.class.getResource("square_figure-view.fxml"));
        FXMLLoader fxmlLoaderperimetrfigure = new FXMLLoader(FiguresApp.class.getResource("perimeter_figure-view.fxml"));
        VBox root = fxmlLoadermain.load();
        fxmlLoaderaddfigure.load();
        fxmlLoadermovefigure.load();
        fxmlLoaderdeletefigure.load();
        fxmlLoadercrossfigure.load();
        fxmlLoadersquarefigure.load();
        fxmlLoaderperimetrfigure.load();


        // Получаем контроллер
        MainController controller = fxmlLoadermain.getController();
        AddFiguresController controller1 = fxmlLoaderaddfigure.getController();
        MoveFiguresController controller2 = fxmlLoadermovefigure.getController();
        DeleteFiguresController controller3 = fxmlLoaderdeletefigure.getController();
        CrossFiguresController controller4 = fxmlLoadercrossfigure.getController();
        SquareFigureController controller5 = fxmlLoadersquarefigure.getController();
        PerimeterFigureController controller6 = fxmlLoaderperimetrfigure.getController();


        // Устанавливаем зависимость
        controller.setControllers(controller4,controller1,controller2,controller3);
        controller1.setControllers(controller,controller4, controller2,controller3);
        controller2.setControllers(controller,controller1, controller4,controller3);
        controller3.setControllers(controller,controller1, controller4,controller2);
        controller4.setControllers(controller,controller1, controller2,controller3);
        controller5.setControllers(controller);
        controller6.setControllers(controller);

        // Устанавливаем зависимость
        controller.setApplication(this);
        controller1.setApplication(this);
        controller2.setApplication(this);
        controller3.setApplication(this);
        controller4.setApplication(this);
        controller5.setApplication(this);
        controller6.setApplication(this);


        Scene scene = new Scene(root, 950, 700);
        scene.getStylesheets().add(Objects.requireNonNull(getClass().getResource("styles.css")).toExternalForm());
        stage.setTitle("FiguresApp");
        stage.setScene(scene);
        stage.show();

        Canvas canvas = (Canvas) root.lookup("#canvas");
        graphicsContext = canvas.getGraphicsContext2D();
        
        image = new WritableImage((int) canvas.getWidth(), (int) canvas.getHeight());
        graphicsContext = canvas.getGraphicsContext2D();
        graphicsContext.drawImage(image, 0, 0);

        // Draw X and Y axes
        drawAxes(canvas.getWidth(), canvas.getHeight());
    }

    public void drawAxes(double canvasWidth, double canvasHeight) {
        graphicsContext.setStroke(Color.GRAY);
        graphicsContext.setLineWidth(1);

        // X-axis
        graphicsContext.strokeLine(0, canvasHeight / 2, canvasWidth, canvasHeight / 2);

        // Y-axis
        graphicsContext.strokeLine(canvasWidth / 2, 0, canvasWidth / 2, canvasHeight);
    }

    public void setFiguresCount(int value) {
        Storage.figuresCount = value;
    }


    public List<IShape> getListFigures(){
        return Storage.listFigures;
    }

    public static void main(String[] args) {
        launch();
    }
}
