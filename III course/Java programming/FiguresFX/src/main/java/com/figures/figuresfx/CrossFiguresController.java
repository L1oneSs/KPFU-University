package com.figures.figuresfx;

import com.figures.exceptions.NullInputException;
import com.figures.figures.*;
import com.figures.figures.points.Point2D;
import com.figures.interfaces.IShape;
import com.figures.storage.Storage;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Alert;
import javafx.scene.control.ComboBox;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.util.ArrayList;
import java.util.List;

public class CrossFiguresController {
    public static List<IShape> listFigures = new ArrayList<>();
    public static List<String> names = new ArrayList<>();
    @FXML
    public ComboBox<String> comboBox5;
    @FXML
    public ComboBox<String> comboBox6;

    @FXML
    public ComboBox<String> comboBox7;

    private MainController mainController;
    private AddFiguresController addFiguresController;
    private MoveFiguresController moveFiguresController;
    private DeleteFiguresController deleteFiguresController;

    private FiguresApp application;

    public void setApplication(FiguresApp application) {
        this.application = application;
    }

    public void setControllers(MainController mainController, AddFiguresController addFiguresController, MoveFiguresController moveFiguresController, DeleteFiguresController deleteFiguresController) {
        this.mainController = mainController;
        this.addFiguresController = addFiguresController;
        this.moveFiguresController = moveFiguresController;
        this.deleteFiguresController = deleteFiguresController;
    }

    public void initialize(){
        comboBox7.getItems().addAll("Отрезок",
                "Ломанная",
                "Окружность",
                "Многоугольник",
                "Треугольник",
                "Четырёхугольник",
                "Прямоугольник",
                "Трапеция");
    }

    @FXML
    public void comboBox7_move(ActionEvent actionEvent) {
        listFigures.clear();
        names.clear();
        ObservableList<String> items = FXCollections.observableArrayList();
        String value = comboBox7.getValue();
        switch (value){
            case "Отрезок":
                items.clear();
                for(int i = 0; i < Storage.figuresCount; i++){
                    if(Storage.nameFigures.get(i).equals("Отрезок")){
                        items.add("Отрезок " + String.valueOf(Storage.listFigures.get(i)));
                        listFigures.add(Storage.listFigures.get(i));
                    }
                }
                comboBox5.setItems(items);
                comboBox6.setItems(items);
                break;
            case "Ломанная":
                items.clear();
                for(int i = 0; i < Storage.figuresCount; i++){
                    if(Storage.nameFigures.get(i).equals("Ломанная")){
                        items.add("Ломанная " + String.valueOf(Storage.listFigures.get(i)));
                        listFigures.add(Storage.listFigures.get(i));
                    }
                }
                comboBox5.setItems(items);
                comboBox6.setItems(items);
                break;
            case "Окружность":
                items.clear();
                for(int i = 0; i < Storage.figuresCount; i++){
                    if(Storage.nameFigures.get(i).equals("Окружность")){
                        items.add("Окружность " + String.valueOf(Storage.listFigures.get(i)));
                        listFigures.add(Storage.listFigures.get(i));
                    }
                }
                comboBox5.setItems(items);
                comboBox6.setItems(items);
                break;
            case "Многоугольник":
                items.clear();
                for(int i = 0; i < Storage.figuresCount; i++){
                    if(Storage.nameFigures.get(i).equals("Многоугольник")){
                        items.add("Многоугольник " + String.valueOf(Storage.listFigures.get(i)));
                        listFigures.add(Storage.listFigures.get(i));
                    }
                }
                comboBox5.setItems(items);
                comboBox6.setItems(items);
                break;
            case "Треугольник":
                items.clear();
                for(int i = 0; i < Storage.figuresCount; i++){
                    if(Storage.nameFigures.get(i).equals("Треугольник")){
                        items.add("Треугольник " + String.valueOf(Storage.listFigures.get(i)));
                        listFigures.add(Storage.listFigures.get(i));
                    }
                }
                comboBox5.setItems(items);
                comboBox6.setItems(items);
                break;
            case "Четырёхугольник":
                items.clear();
                for(int i = 0; i < Storage.figuresCount; i++){
                    if(Storage.nameFigures.get(i).equals("Четырёхугольник")){
                        items.add("Четырёхугольник " + String.valueOf(Storage.listFigures.get(i)));
                        listFigures.add(Storage.listFigures.get(i));
                    }
                }
                comboBox5.setItems(items);
                comboBox6.setItems(items);
                break;
            case "Прямоугольник":
                items.clear();
                for(int i = 0; i < Storage.figuresCount; i++){
                    if(Storage.nameFigures.get(i).equals("Прямоугольник")){
                        items.add("Прямоугольник " + String.valueOf(Storage.listFigures.get(i)));
                        listFigures.add(Storage.listFigures.get(i));
                    }
                }
                comboBox5.setItems(items);
                comboBox6.setItems(items);
                break;
            case "Трапеция":
                items.clear();
                for(int i = 0; i < Storage.figuresCount; i++){
                    if(Storage.nameFigures.get(i).equals("Трапеция")){
                        items.add("Трапеция " + String.valueOf(Storage.listFigures.get(i)));
                        listFigures.add(Storage.listFigures.get(i));
                    }
                }
                comboBox5.setItems(items);
                comboBox6.setItems(items);
                break;
        }
    }
    @FXML
    private void button7_Click(ActionEvent actionEvent){
        try {
            if (comboBox5.getSelectionModel().getSelectedIndex() == -1 || comboBox6.getSelectionModel().getSelectedIndex() == -1) {
                throw new NullInputException();
            }
            if (comboBox5.getSelectionModel().getSelectedIndex() == comboBox6.getSelectionModel().getSelectedIndex()) {
                throw new EqualsException();
            }
            if(moveFiguresController.comboBox3.getSelectionModel().getSelectedIndex() < 0){
                moveFiguresController.comboBox3.getSelectionModel().select(-1);
            }
            if (deleteFiguresController.comboBox4.getSelectionModel().getSelectedIndex() < 0) {
                deleteFiguresController.comboBox4.getSelectionModel().select(0);
            }
            if (comboBox5.getSelectionModel().getSelectedIndex() < 0) {
                comboBox5.getSelectionModel().select(0);
            }
            if (comboBox6.getSelectionModel().getSelectedIndex() < 0) {
                comboBox6.getSelectionModel().select(0);
            }
            if(listFigures.get(comboBox5.getSelectionModel().getSelectedIndex()).cross(listFigures.get(comboBox6.getSelectionModel().getSelectedIndex()))){
                mainController.label61.setVisible(true);
                mainController.textBox41.setVisible(true);
                mainController.label61.setText("Пересечение:");
                mainController.textBox41.setText("Пересекаются.");
            }
            else{
                mainController.label61.setVisible(true);
                mainController.textBox41.setVisible(true);
                mainController.label61.setText("Пересечение:");
                mainController.textBox41.setText("Не пересекаются.");
            }
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
            mainController.draw(listFigures.get(comboBox5.getSelectionModel().getSelectedIndex()), Color.RED);
            mainController.draw(listFigures.get(comboBox6.getSelectionModel().getSelectedIndex()), Color.RED);
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Успех");
            alert.setHeaderText(null);
            alert.setContentText("Сравнение было выполнено успешно");

            alert.showAndWait();
        }
        catch (EqualsException ex) {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setTitle("Ошибка");
            alert.setHeaderText(null);
            alert.setContentText("Вы пытаетесь сравнить одну и ту же фигуру");
            alert.showAndWait();
        } catch (NullInputException ex) {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setTitle("NullInputException");
            alert.setHeaderText(null);
            alert.setContentText(ex.toString());
            alert.showAndWait();
        } catch (IllegalArgumentException ex) {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setTitle("IllegalArgumentException ex");
            alert.setHeaderText(null);
            alert.setContentText(ex.toString());
            alert.showAndWait();
        }
    }

    public void CancelButton_Click(ActionEvent actionEvent) {
        Stage stage = (Stage) ((Node) actionEvent.getSource()).getScene().getWindow();

        // Закрыть текущую сцену (форму)
        stage.close();
    }


}
