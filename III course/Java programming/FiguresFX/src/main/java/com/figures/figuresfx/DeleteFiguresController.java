package com.figures.figuresfx;

import com.figures.exceptions.NullInputException;
import com.figures.storage.Storage;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

public class DeleteFiguresController {
    @FXML
    public ComboBox<String> comboBox4;
    private MainController mainController;
    private AddFiguresController addFiguresController;
    private CrossFiguresController crossFiguresController;
    private MoveFiguresController moveFiguresController;

    public void setControllers(MainController mainController, AddFiguresController addFiguresController, CrossFiguresController crossFiguresController, MoveFiguresController moveFiguresController) {
        this.mainController = mainController;
        this.addFiguresController = addFiguresController;
        this.crossFiguresController = crossFiguresController;
        this.moveFiguresController = moveFiguresController;
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
                    comboBox4.getItems().add("Окружность: " + "Circle" + Storage.getListFigures().get(i).toString());
                    break;
                case "Отрезок":
                    comboBox4.getItems().add("Отрезок: " + "Segment" + Storage.getListFigures().get(i).toString());
                    break;
                case "Ломанная": // Если фигура - полилиния
                case "Многоугольник": // Если фигура - правильный n-угольник
                case "Четырёхугольник": // Если фигура - квадрат
                case "Треугольник": // Если фигура - равнобедренный треугольник
                case "Трапеция": // Если фигура - трапеция
                case "Прямоугольник": // Если фигура - прямоугольник

                    // Добавление фигуры в список в зависимости от типа
                    if (figure == "Ломанная") {
                        comboBox4.getItems().add("Ломанная: " + "Polyline" + Storage.getListFigures().get(i).toString());
                    }
                    if (figure == "Многоугольник") {
                        comboBox4.getItems().add("Многоугольник: " + "NGon" + Storage.getListFigures().get(i).toString());
                    }
                    if (figure == "Четырёхугольник") {
                        comboBox4.getItems().add("Четырёхугольник: " + "QGon" + Storage.getListFigures().get(i).toString());
                    }
                    if (figure == "Треугольник") {
                        comboBox4.getItems().add("Треугольник: " + "TGon" + Storage.getListFigures().get(i).toString());
                    }
                    if (figure == "Трапеция") {
                        comboBox4.getItems().add("Трапеция: " + "Trapeze" + Storage.getListFigures().get(i).toString());
                    }
                    if (figure == "Прямоугольник") {
                        comboBox4.getItems().add("Прямоугольник: " + "Rectangle" + Storage.getListFigures().get(i).toString());
                    }
                    break;
            }
        }
    }

    @FXML
    private void button6_Click(ActionEvent actionEvent){
        try {
            if (moveFiguresController.comboBox3.getSelectionModel().getSelectedIndex() == -1 && Storage.getFiguresCount() == 0 || moveFiguresController.comboBox3.getSelectionModel().getSelectedIndex() == 0 && Storage.getFiguresCount() == 0) {
                throw new NullInputException();
            }
            if (moveFiguresController.comboBox3.getSelectionModel().getSelectedIndex() < 0) {
                moveFiguresController.comboBox3.getSelectionModel().select(0);
            }
            if(Storage.getFiguresCount() == 0){
                comboBox4.getSelectionModel().select(-1);
            }
            else if (comboBox4.getSelectionModel().getSelectedIndex() < 0) {
                comboBox4.getSelectionModel().select(0);
            }
            if (crossFiguresController.comboBox5.getSelectionModel().getSelectedIndex() < 0) {
                crossFiguresController.comboBox5.getSelectionModel().select(0);
            }
            if (crossFiguresController.comboBox6.getSelectionModel().getSelectedIndex() < 0) {
                crossFiguresController.comboBox6.getSelectionModel().select(0);
            }
            if(comboBox4.getSelectionModel().getSelectedIndex() != -1){
                Storage.getListFigures().remove(comboBox4.getSelectionModel().getSelectedIndex());
                Storage.nameFigures.remove(comboBox4.getSelectionModel().getSelectedIndex());
                comboBox4.getItems().remove(comboBox4.getSelectionModel().getSelectedIndex());
                if (mainController.canvas != null) {
                    // Очищаем содержимое холста (canvas) с белым цветом
                    GraphicsContext gc = mainController.canvas.getGraphicsContext2D();
                    gc.setFill(Color.WHITE);
                    gc.clearRect(0, 0, mainController.canvas.getWidth(), mainController.canvas.getHeight());

                    // Вызываем метод requestFocus(), чтобы перерисовать холст
                    mainController.canvas.requestFocus();
                }
                assert mainController.canvas != null;
                application.drawAxes(mainController.canvas.getWidth(), mainController.canvas.getHeight());
                for(int i = 0; i < Storage.getListFigures().size(); i++){
                    mainController.draw(Storage.getListFigures().get(i), Color.BLACK);
                }
                Storage.decFiguresCount();
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
            mainController.label61.setText("");
            mainController.textBox41.setText("");
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Успех");
            alert.setHeaderText(null);
            alert.setContentText("Удаление завершено");

            alert.showAndWait();
        }
        catch (NullInputException ex) {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setTitle("Ошибка");
            alert.setHeaderText("NullInputException");
            alert.setContentText(ex.toString());
            alert.showAndWait();
        } catch (IllegalArgumentException ex) {
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
