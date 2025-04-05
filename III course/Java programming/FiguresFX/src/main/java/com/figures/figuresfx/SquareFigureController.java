package com.figures.figuresfx;

import com.figures.storage.Storage;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Alert;
import javafx.scene.control.ComboBox;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

public class SquareFigureController {

    @FXML
    public ComboBox<String> comboBoxs;

    private MainController mainController;


    public void setControllers(MainController mainController) {
        this.mainController = mainController;
    }

    private FiguresApp application;

    public void setApplication(FiguresApp application) {
        this.application = application;
    }

    public void initialize(){
        for(int i = 0; i < Storage.getListFigures().size(); i++) {
            String figure = Storage.nameFigures.get(i);
            switch (figure) {
                case "Окружность":
                    comboBoxs.getItems().add("Окружность: " + "Circle" + Storage.getListFigures().get(i).toString());
                    break;
                case "Отрезок":
                    comboBoxs.getItems().add("Отрезок: " + "Segment" + Storage.getListFigures().get(i).toString());
                    break;
                case "Ломанная": // Если фигура - полилиния
                case "Многоугольник": // Если фигура - правильный n-угольник
                case "Четырёхугольник": // Если фигура - квадрат
                case "Треугольник": // Если фигура - равнобедренный треугольник
                case "Трапеция": // Если фигура - трапеция
                case "Прямоугольник": // Если фигура - прямоугольник

                    // Добавление фигуры в список в зависимости от типа
                    if (figure == "Ломанная") {

                        comboBoxs.getItems().add("Ломанная: " + "Polyline" + Storage.getListFigures().get(i).toString());
                    }
                    if (figure == "Многоугольник") {

                        comboBoxs.getItems().add("Многоугольник: " + "NGon" + Storage.getListFigures().get(i).toString());
                    }
                    if (figure == "Четырёхугольник") {

                        comboBoxs.getItems().add("Четырёхугольник: " + "QGon" + Storage.getListFigures().get(i).toString());
                    }
                    if (figure == "Треугольник") {

                        comboBoxs.getItems().add("Треугольник: " + "TGon" + Storage.getListFigures().get(i).toString());
                    }
                    if (figure == "Трапеция") {

                        comboBoxs.getItems().add("Трапеция: " + "Trapeze" + Storage.getListFigures().get(i).toString());
                    }
                    if (figure == "Прямоугольник") {

                        comboBoxs.getItems().add("Прямоугольник: " + "Rectangle" + Storage.getListFigures().get(i).toString());
                    }
                    break;
            }
        }
        String type;
        Storage.nameFigures.clear();
        for(int j = 0; j < Storage.figuresCount; j++ )
        {
            type = Storage.getListFigures().get(j).getClass().getSimpleName();
            type = type.replace("FiguresFX.", "");
            if ("Circle".equals(type)) {
                Storage.nameFigures.add("Окружность");
            } else if ("NGon".equals(type)) {
                Storage.nameFigures.add("Многоугольник");
            } else if ("Trapeze".equals(type)) {
                Storage.nameFigures.add("Трапеция");
            } else if ("Rectangle".equals(type)) {
                Storage.nameFigures.add("Прямоугольник");
            } else if ("TGon".equals(type)) {
                Storage.nameFigures.add("Треугольник");
            } else if ("Polyline".equals(type)) {
                Storage.nameFigures.add("Ломанная");
            } else if ("QGon".equals(type)) {
                Storage.nameFigures.add("Четырёхугольник");
            } else if ("Segment".equals(type)) {
                Storage.nameFigures.add("Отрезок");
            }
        }
    }

    @FXML
    public void buttons_Click(ActionEvent actionEvent) {
        try
        {
            Canvas canvas = mainController.canvas;
            GraphicsContext gc = mainController.canvas.getGraphicsContext2D();
            gc.clearRect(0, 0, canvas.getWidth(), canvas.getHeight());
            application.drawAxes(canvas.getWidth(), canvas.getHeight());
            for(int i = 0; i < Storage.figuresCount; i++){
                mainController.draw(Storage.getListFigures().get(i), Color.BLACK);
            }
            double square = Storage.listFigures.get(comboBoxs.getSelectionModel().getSelectedIndex()).square();

            mainController.label61.setText("Площадь: ");
            mainController.textBox41.setText(String.valueOf(square));
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Успех");
            alert.setHeaderText(null);
            alert.setContentText("Площадь подсчитана");
            alert.showAndWait();

        }
        catch(IllegalArgumentException ex)
        {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setTitle("Ошибка");
            alert.setHeaderText("IllegalArgumentException ex");
            alert.setContentText(ex.getMessage());
            alert.showAndWait();
        }
}



    public void CancelButton_Click(ActionEvent actionEvent) {
        Stage stage = (Stage) ((Node) actionEvent.getSource()).getScene().getWindow();

        // Закрыть текущую сцену (форму)
        stage.close();
    }
}
