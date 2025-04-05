package com.figures.figuresfx;

import com.figures.exceptions.NullInputException;
import com.figures.figures.*;
import com.figures.figures.points.Point2D;
import com.figures.figuresfx.FiguresApp;
import com.figures.interfaces.IShape;
import com.figures.storage.Storage;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.SnapshotParameters;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.*;
import javafx.scene.image.WritableImage;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.stage.Modality;
import javafx.stage.Stage;

import javafx.event.ActionEvent;
import javafx.scene.SnapshotParameters;
import javafx.scene.canvas.Canvas;
import javafx.scene.control.Alert;
import javafx.scene.image.WritableImage;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.scene.SnapshotParameters;
import javafx.scene.canvas.Canvas;
import javafx.scene.control.Alert;
import javafx.scene.image.WritableImage;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;


import java.io.*;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class MainController
{

    public MainController(){}

    private FiguresApp application;

    public void setApplication(FiguresApp application) {
        this.application = application;
    }

    private CrossFiguresController crossFiguresController;
    private AddFiguresController addFiguresController;
    private MoveFiguresController moveFiguresController;
    private DeleteFiguresController deleteFiguresController;

    public void setControllers(CrossFiguresController crossFiguresController, AddFiguresController addFiguresController, MoveFiguresController moveFiguresController, DeleteFiguresController deleteFiguresController) {
        this.crossFiguresController = crossFiguresController;
        this.addFiguresController = addFiguresController;
        this.moveFiguresController = moveFiguresController;
        this.deleteFiguresController = deleteFiguresController;
    }


    @FXML
    public Canvas canvas;
    @FXML
    public Label label61;
    @FXML
    public TextField textBox41;
    @FXML
    private Button fbutton2;
    @FXML
    private Button fbutton3;
    @FXML
    private Button fbutton4;
    @FXML
    private Button fbutton5;
    @FXML
    private Button fbutton6;
    @FXML
    private Button fbutton7;



    public void initialize() {}


    @FXML
    private void button1_Click(ActionEvent actionEvent){
        if (canvas != null) {
            // Очищаем содержимое холста (canvas) с белым цветом
            GraphicsContext gc = canvas.getGraphicsContext2D();
            gc.setFill(Color.WHITE);
            gc.clearRect(0, 0, canvas.getWidth(), canvas.getHeight());

            // Вызываем метод requestFocus(), чтобы перерисовать холст
            canvas.requestFocus();
        }
        assert canvas != null;
        application.drawAxes(canvas.getWidth(), canvas.getHeight());
        application.getListFigures().clear();
        application.setFiguresCount(0);
        moveFiguresController.comboBox3.getItems().clear();
        deleteFiguresController.comboBox4.getItems().clear();
        crossFiguresController.comboBox5.getItems().clear();
        crossFiguresController.comboBox6.getItems().clear();
        label61.setText("");
        textBox41.setText("");
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Успех");
        alert.setHeaderText(null);
        alert.setContentText("Все фигуры удалены");

        alert.showAndWait();
    }

    @FXML
    private void fbutton2_Click(ActionEvent actionEvent){
        // Проверяем, что listFigures не пустой
        if (Storage.getListFigures().isEmpty()) {
            // Выводим Alert, если listFigures пустой
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Ошибка");
            alert.setHeaderText(null);
            alert.setContentText("Добавьте хотя бы одну фигуру");
            alert.showAndWait();
            return; // Прекращаем выполнение метода, так как нет фигур для сохранения
        }
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("square_figure-view.fxml"));
            Parent root = loader.load();
            SquareFigureController controller1 = loader.getController();


            controller1.setControllers(this);

            controller1.setApplication(application);


            // Создайте новое модальное окно
            Stage moveFigureStage = new Stage();
            moveFigureStage.initModality(Modality.APPLICATION_MODAL); // Сделать окно модальным
            moveFigureStage.setTitle("Площадь фигуры");
            moveFigureStage.setScene(new Scene(root));

            // Заблокируйте взаимодействие с главным окном
            moveFigureStage.initOwner(fbutton2.getScene().getWindow());

            // Отобразите окно и дождитесь его закрытия
            moveFigureStage.showAndWait();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void fbutton3_Click(ActionEvent actionEvent) {
        // Проверяем, что listFigures не пустой
        if (Storage.getListFigures().isEmpty()) {
            // Выводим Alert, если listFigures пустой
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Ошибка");
            alert.setHeaderText(null);
            alert.setContentText("Добавьте хотя бы одну фигуру");
            alert.showAndWait();
            return; // Прекращаем выполнение метода, так как нет фигур для сохранения
        }
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("perimeter_figure-view.fxml"));
            Parent root = loader.load();
            PerimeterFigureController controller1 = loader.getController();


            controller1.setControllers(this);

            controller1.setApplication(application);


            // Создайте новое модальное окно
            Stage moveFigureStage = new Stage();
            moveFigureStage.initModality(Modality.APPLICATION_MODAL); // Сделать окно модальным
            moveFigureStage.setTitle("Периметр фигуры");
            moveFigureStage.setScene(new Scene(root));

            // Заблокируйте взаимодействие с главным окном
            moveFigureStage.initOwner(fbutton3.getScene().getWindow());

            // Отобразите окно и дождитесь его закрытия
            moveFigureStage.showAndWait();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @FXML
    public void fbutton4_click() {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("add_figure-view.fxml"));
            Parent root = loader.load();
            AddFiguresController controller1 = loader.getController();

            FXMLLoader loader2 = new FXMLLoader(getClass().getResource("move_figure-view.fxml"));
            loader2.load();
            MoveFiguresController controller2 = loader2.getController();

            FXMLLoader loader3 = new FXMLLoader(getClass().getResource("delete_figure-view.fxml"));
            loader3.load();
            DeleteFiguresController controller3 = loader3.getController();

            FXMLLoader loader4 = new FXMLLoader(getClass().getResource("cross_figure-view.fxml"));
            loader4.load();
            CrossFiguresController controller4 = loader4.getController();

            controller1.setControllers(this, controller4, controller2, controller3);

            controller1.setApplication(application);
            controller2.setApplication(application);
            controller3.setApplication(application);
            controller4.setApplication(application);

            // Создайте новое модальное окно
            Stage moveFigureStage = new Stage();
            moveFigureStage.initModality(Modality.APPLICATION_MODAL); // Сделать окно модальным
            moveFigureStage.setTitle("Добавление фигуры");
            moveFigureStage.setScene(new Scene(root));

            // Заблокируйте взаимодействие с главным окном
            moveFigureStage.initOwner(fbutton4.getScene().getWindow());

            // Отобразите окно и дождитесь его закрытия
            moveFigureStage.showAndWait();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @FXML
    public void fbutton5_click(ActionEvent actionEvent) {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("add_figure-view.fxml"));
            loader.load();
            AddFiguresController controller1 = loader.getController();


            FXMLLoader loader2 = new FXMLLoader(getClass().getResource("move_figure-view.fxml"));
            Parent root = loader2.load();
            MoveFiguresController controller2 = loader2.getController();


            FXMLLoader loader3 = new FXMLLoader(getClass().getResource("delete_figure-view.fxml"));
            loader3.load();
            DeleteFiguresController controller3 = loader3.getController();

            FXMLLoader loader4 = new FXMLLoader(getClass().getResource("cross_figure-view.fxml"));
            loader4.load();
            CrossFiguresController controller4 = loader4.getController();

            controller2.setControllers(this, controller1, controller4, controller3);

            controller1.setApplication(application);
            controller2.setApplication(application);
            controller3.setApplication(application);
            controller4.setApplication(application);

            // Создайте новое модальное окно
            Stage moveFigureStage = new Stage();
            moveFigureStage.initModality(Modality.APPLICATION_MODAL); // Сделать окно модальным
            moveFigureStage.setTitle("Перемещение фигуры");
            moveFigureStage.setScene(new Scene(root));

            // Заблокируйте взаимодействие с главным окном
            moveFigureStage.initOwner(fbutton5.getScene().getWindow());

            // Отобразите окно и дождитесь его закрытия
            moveFigureStage.showAndWait();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @FXML
    public void fbutton6_click(ActionEvent actionEvent) {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("add_figure-view.fxml"));
            loader.load();
            AddFiguresController controller1 = loader.getController();


            FXMLLoader loader2 = new FXMLLoader(getClass().getResource("move_figure-view.fxml"));
            loader2.load();
            MoveFiguresController controller2 = loader2.getController();


            FXMLLoader loader3 = new FXMLLoader(getClass().getResource("delete_figure-view.fxml"));
            Parent root = loader3.load();
            DeleteFiguresController controller3 = loader3.getController();

            FXMLLoader loader4 = new FXMLLoader(getClass().getResource("cross_figure-view.fxml"));
            loader4.load();
            CrossFiguresController controller4 = loader4.getController();

            controller3.setControllers(this, controller1, controller4, controller2);

            controller1.setApplication(application);
            controller2.setApplication(application);
            controller3.setApplication(application);
            controller4.setApplication(application);


            // Создайте новое модальное окно
            Stage moveFigureStage = new Stage();
            moveFigureStage.initModality(Modality.APPLICATION_MODAL); // Сделать окно модальным
            moveFigureStage.setTitle("Удаление фигуры");
            moveFigureStage.setScene(new Scene(root));

            // Заблокируйте взаимодействие с главным окном
            moveFigureStage.initOwner(fbutton6.getScene().getWindow());

            // Отобразите окно и дождитесь его закрытия
            moveFigureStage.showAndWait();




        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @FXML
    public void fbutton7_click(ActionEvent actionEvent) {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("add_figure-view.fxml"));
            loader.load();
            AddFiguresController controller1 = loader.getController();


            FXMLLoader loader2 = new FXMLLoader(getClass().getResource("move_figure-view.fxml"));
            loader2.load();
            MoveFiguresController controller2 = loader2.getController();


            FXMLLoader loader3 = new FXMLLoader(getClass().getResource("delete_figure-view.fxml"));
            loader3.load();
            DeleteFiguresController controller3 = loader3.getController();

            FXMLLoader loader4 = new FXMLLoader(getClass().getResource("cross_figure-view.fxml"));
            Parent root = loader4.load();
            CrossFiguresController controller4 = loader4.getController();

            controller4.setControllers(this, controller1, controller2, controller3);

            controller1.setApplication(application);
            controller2.setApplication(application);
            controller3.setApplication(application);
            controller4.setApplication(application);


            // Создайте новое модальное окно
            Stage moveFigureStage = new Stage();
            moveFigureStage.initModality(Modality.APPLICATION_MODAL); // Сделать окно модальным
            moveFigureStage.setTitle("Пересечение фигур");
            moveFigureStage.setScene(new Scene(root));

            // Заблокируйте взаимодействие с главным окном
            moveFigureStage.initOwner(fbutton7.getScene().getWindow());

            // Отобразите окно и дождитесь его закрытия
            moveFigureStage.showAndWait();




        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public void draw(IShape i, Color color) {
        double[] mas_x = new double[0];
        double[] mas_y = new double[0];
        GraphicsContext gc = canvas.getGraphicsContext2D();
        if (i instanceof Circle) {
            mas_x = new double[101];
            mas_y = new double[101];
            Circle f = (Circle) i;

            for (int j = 0; j <= 100; j++) {
                double x = f.getP().getX(0) + f.getR() * Math.cos(j * 2 * Math.PI / 100);
                double y = f.getP().getX(1) + f.getR() * Math.sin(j * 2 * Math.PI / 100);
                mas_x[j] = x;
                mas_y[j] = y;
            }

        } else if (i instanceof Segment) {
            mas_x = new double[2];
            mas_y = new double[2];
            Segment f = (Segment) i;
            mas_x[0] = f.getStart().getX(0);
            mas_y[0] = f.getStart().getX(1);
            mas_x[1] = f.getFinish().getX(0);
            mas_y[1] = f.getFinish().getX(1);

        } else if (i instanceof Polyline) {
            int q = 0;
            Polyline f = (Polyline) i;
            Point2D[] pointss = f.getP();
            mas_x = new double[pointss.length];
            mas_y = new double[pointss.length];
            for (int j = 0; j < pointss.length; j++) {
                Point2D v = pointss[j];
                mas_x[q] = v.getX(0);
                mas_y[q] = v.getX(1);
                q++;
            }

        } else if (i instanceof NGon) {
            int q = 0;
            NGon f = (NGon) i;
            mas_x = new double[f.getP().length + 1];
            mas_y = new double[f.getP().length + 1];
            for (Point2D v : f.getP()) {
                mas_x[q] = v.getX(0);
                mas_y[q] = v.getX(1);
                q++;
            }
            mas_x[f.getP().length] = f.getP()[0].getX(0);
            mas_y[f.getP().length] = f.getP()[0].getX(1);
        }

        // Коэффициент масштабирования
        double scaleFactor = 8.0;

        // Получаем размеры Canvas
        double canvasWidth = canvas.getWidth();
        double canvasHeight = canvas.getHeight();

        gc.setStroke(color);

        Scale(i, mas_x, mas_y, gc, scaleFactor, canvasWidth, canvasHeight);
    }



    private void Scale(IShape i, double[] mas_x, double[] mas_y, GraphicsContext gc, double scaleFactor, double canvasWidth, double canvasHeight) {
        for (int q = 0; q < mas_x.length - 1; q++) {
            double x1 = mas_x[q] * scaleFactor + canvasWidth / 2;
            double y1 = -mas_y[q] * scaleFactor + canvasHeight / 2;
            double x2 = mas_x[q + 1] * scaleFactor + canvasWidth / 2;
            double y2 = -mas_y[q + 1] * scaleFactor + canvasHeight / 2;
            gc.strokeLine(x1, y1, x2, y2);
        }

        if (i instanceof Polyline) {
            // Дополнительные действия для Polyline, если нужно
        } else {
            double x1 = mas_x[mas_x.length - 1] * scaleFactor + canvasWidth / 2;
            double y1 = -mas_y[mas_y.length - 1] * scaleFactor + canvasHeight / 2;
            double x2 = mas_x[0] * scaleFactor + canvasWidth / 2;
            double y2 = -mas_y[0] * scaleFactor + canvasHeight / 2;
            gc.strokeLine(x1, y1, x2, y2);
        }
    }

    @FXML
    public void button_save_Click(ActionEvent actionEvent) {
        // Проверяем, что список фигур не пуст
        if (Storage.getListFigures().isEmpty()) {
            // Если список пуст, выводим предупреждение и завершаем метод
            showAlert("Ошибка", "Вы еще не добавили ни одной фигуры.");
            return;
        }

        // Задайте относительный путь и имя файла в директории проекта
        String relativePath = "save_figures.txt"; // Имя файла и относительный путь

        // Создаем файл в указанном пути
        File file = new File(relativePath);

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(file))) {
            writer.write(String.valueOf(Storage.figuresCount));
            writer.newLine();
            // Записываем каждую фигуру в файл на отдельной строке
            for (int i = 0; i < Storage.listFigures.size(); i++) {
                writer.write(Storage.nameFigures.get(i));
                writer.newLine();
                writer.write( Storage.listFigures.get(i).toString());
                writer.newLine(); // Переходим на новую строку
            }
            showAlert("Успех", "Фигуры успешно сохранены в файл: " + file.getCanonicalPath());
        } catch (IOException e) {
            e.printStackTrace();
            showAlert("Ошибка", "Произошла ошибка при сохранении данных.");
        }
    }

    @FXML
    public void button_loadFile_Click(ActionEvent actionEvent) {
        try {
            Storage.listFigures.clear();
            Storage.nameFigures.clear();
            BufferedReader reader = new BufferedReader(new FileReader("load_figures.txt"));
            String n = reader.readLine();
            Storage.figuresCount = Integer.parseInt(n);

            String line;

            while ((line = reader.readLine()) != null) {
                String[] values = line.split(" ");
                String figure = values[0];

                switch (figure) {
                    case "Circle":
                        Storage.nameFigures.add("Окружность");
                        Storage.listFigures.add(new Circle(new Point2D(new double[]{Double.parseDouble(values[1]), Double.parseDouble(values[2])}), Double.parseDouble(values[3])));
                        break;
                    case "Segment":
                        Storage.nameFigures.add("Отрезок");
                        Storage.listFigures.add(new Segment(new Point2D(new double[]{Double.parseDouble(values[1]), Double.parseDouble(values[2])}),
                                new Point2D(new double[]{Double.parseDouble(values[3]), Double.parseDouble(values[4])})));
                        break;
                    case "Polyline":
                    case "NGon":
                    case "QGon":
                    case "TGon":
                    case "Trapeze":
                    case "Rectangle":
                        int k = Integer.parseInt(values[1]);
                        Point2D[] pr = new Point2D[k];
                        for (int i = 0, j = 2; i < k; i++, j += 2) {
                            pr[i] = new Point2D(new double[]{Double.parseDouble(values[j]), Double.parseDouble(values[j + 1])});
                        }
                        if (figure.equals("Polyline"))
                        {
                            Storage.nameFigures.add("Ломанная");
                            Storage.listFigures.add(new Polyline(pr));
                        }
                        if (figure.equals("NGon"))
                        {
                            Storage.nameFigures.add("Многоугольник");
                            Storage.listFigures.add(new NGon(pr));
                        }
                        if (figure.equals("QGon"))
                        {
                            Storage.nameFigures.add("Четырёхугольник");
                            Storage.listFigures.add(new QGon(pr));
                        }
                        if (figure.equals("TGon"))
                        {
                            Storage.nameFigures.add("Треугольник");
                            Storage.listFigures.add(new TGon(pr));
                        }
                        if (figure.equals("Trapeze"))
                        {
                            Storage.nameFigures.add("Трапеция");
                            Storage.listFigures.add(new Trapeze(pr));
                        }
                        if (figure.equals("Rectangle"))
                        {
                            Storage.nameFigures.add("Прямоугольник");
                            Storage.listFigures.add(new Rectangle(pr));
                        }
                        break;
                    default:
                        System.out.println("Введён неверный тип фигуры: " + figure);
                        break;
                }
            }
            reader.close();
            GraphicsContext gc = canvas.getGraphicsContext2D();
            gc.clearRect(0, 0, canvas.getWidth(), canvas.getHeight());
            application.drawAxes(canvas.getWidth(), canvas.getHeight());
            for(int i = 0; i < Storage.figuresCount; i++){
                draw(Storage.getListFigures().get(i), Color.BLACK);
            }
            showAlert("Успех", "Фигуры успешно загружены");
        } catch (IOException ex) {
            showAlert("Ошибка", "Произошла ошибка при сохранении данных.");
        }
    }

    @FXML
    public void button_saveIMG_Click(ActionEvent actionEvent) {
        // Проверяем, что listFigures не пустой
        if (Storage.getListFigures().isEmpty()) {
            // Выводим Alert, если listFigures пустой
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Ошибка");
            alert.setHeaderText(null);
            alert.setContentText("Добавьте хотя бы одну фигуру");
            alert.showAndWait();
            return; // Прекращаем выполнение метода, так как нет фигур для сохранения
        }

        // Создаем объект класса WritableImage, чтобы сохранить содержимое Canvas в изображении
        int width = (int) canvas.getWidth();
        int height = (int) canvas.getHeight();
        WritableImage writableImage = new WritableImage(width, height);
        SnapshotParameters parameters = new SnapshotParameters();
        canvas.snapshot(parameters, writableImage);

        // Указываем путь и имя файла для сохранения
        String fileName = "saved_image.png";
        File file = new File(fileName);

        try {
            // Создаем BufferedImage из WritableImage
            BufferedImage bufferedImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);
            for (int x = 0; x < width; x++) {
                for (int y = 0; y < height; y++) {
                    bufferedImage.setRGB(x, y, writableImage.getPixelReader().getArgb(x, y));
                }
            }

            // Сохраняем изображение
            ImageIO.write(bufferedImage, "png", file);

            // Выводим сообщение об успешном сохранении
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Сохранено");
            alert.setHeaderText(null);
            alert.setContentText("Изображение успешно сохранено в " + fileName);
            alert.showAndWait();
        } catch (IOException e) {
            e.printStackTrace();
            // В случае ошибки сохранения выводим сообщение об ошибке
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Ошибка");
            alert.setHeaderText(null);
            alert.setContentText("Произошла ошибка при сохранении изображения");
            alert.showAndWait();
        }
    }



    private void showAlert(String title, String content) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(content);
        alert.showAndWait();
    }

}