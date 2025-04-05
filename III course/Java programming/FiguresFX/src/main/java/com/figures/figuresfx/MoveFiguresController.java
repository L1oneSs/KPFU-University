package com.figures.figuresfx;

import com.figures.exceptions.NullInputException;
import com.figures.figures.points.Point2D;
import com.figures.storage.Storage;
import javafx.collections.FXCollections;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.*;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.util.Objects;

public class MoveFiguresController {
    @FXML
    private Spinner<String> domainUpDown1;
    @FXML
    private Pane panel1;

    @FXML
    public ComboBox<String> comboBox2;
    @FXML
    public ComboBox<String> comboBox3;

    @FXML
    private TextField textBox38;
    @FXML
    private TextField textBox39;
    @FXML
    private TextField textBox40;
    @FXML
    private Pane pn111;
    @FXML
    private Pane pn222;
    @FXML
    private Pane pn333;

    private MainController mainController;
    private AddFiguresController addFiguresController;
    private CrossFiguresController crossFiguresController;
    private DeleteFiguresController deleteFiguresController;

    public void setControllers(MainController mainController, AddFiguresController addFiguresController, CrossFiguresController crossFiguresController, DeleteFiguresController deleteFiguresController) {
        this.mainController = mainController;
        this.addFiguresController = addFiguresController;
        this.crossFiguresController = crossFiguresController;
        this.deleteFiguresController = deleteFiguresController;
    }

    private FiguresApp application;

    public void setApplication(FiguresApp application) {
        this.application = application;
    }
    
    public void initialize(){
        comboBox2.getItems().addAll("Сдвиг",
                "Поворот",
                "Симметрия"
        );
                String[] items = {"x", "y"};
        SpinnerValueFactory<String> valueFactory_dup = new SpinnerValueFactory.ListSpinnerValueFactory<>(FXCollections.observableArrayList(items));
        domainUpDown1.setValueFactory(valueFactory_dup);

        for(int i = 0; i < Storage.getListFigures().size(); i++) {
            String figure = Storage.nameFigures.get(i);
            switch (figure) {
                case "Окружность":
                    comboBox3.getItems().add("Окружность: " + "Circle" + Storage.getListFigures().get(i).toString());
                    //deleteFiguresController.comboBox4.getItems().add("Окружность: " + "Circle" + Storage.getListFigures().get(Storage.getFiguresCount()).toString());
                    break;
                case "Отрезок":
                    comboBox3.getItems().add("Отрезок: " + "Segment" + Storage.getListFigures().get(i).toString());
                    //deleteFiguresController.comboBox4.getItems().add("Отрезок: " + "Segment" + Storage.getListFigures().get(Storage.getFiguresCount()).toString());
                    break;
                case "Ломанная": // Если фигура - полилиния
                case "Многоугольник": // Если фигура - правильный n-угольник
                case "Четырёхугольник": // Если фигура - квадрат
                case "Треугольник": // Если фигура - равнобедренный треугольник
                case "Трапеция": // Если фигура - трапеция
                case "Прямоугольник": // Если фигура - прямоугольник

                    // Добавление фигуры в список в зависимости от типа
                    if (figure == "Ломанная") {

                        comboBox3.getItems().add("Ломанная: " + "Polyline" + Storage.getListFigures().get(i).toString());
                        //deleteFiguresController.comboBox4.getItems().add("Ломанная: " + "Polyline" + Storage.getListFigures().get(Storage.getFiguresCount()).toString());
                    }
                    if (figure == "Многоугольник") {

                        comboBox3.getItems().add("Многоугольник: " + "NGon" + Storage.getListFigures().get(i).toString());
                        //deleteFiguresController.comboBox4.getItems().add("Многоугольник: " + "NGon" + Storage.getListFigures().get(Storage.getFiguresCount()).toString());
                    }
                    if (figure == "Четырёхугольник") {

                        comboBox3.getItems().add("Четырёхугольник: " + "QGon" + Storage.getListFigures().get(i).toString());
                        //deleteFiguresController.comboBox4.getItems().add("Четырёхугольник: " + "QGon" + Storage.getListFigures().get(Storage.getFiguresCount()).toString());
                    }
                    if (figure == "Треугольник") {

                        comboBox3.getItems().add("Треугольник: " + "TGon" + Storage.getListFigures().get(i).toString());
                        //deleteFiguresController.comboBox4.getItems().add("Треугольник: " + "TGon" + Storage.getListFigures().get(Storage.getFiguresCount()).toString());
                    }
                    if (figure == "Трапеция") {

                        comboBox3.getItems().add("Трапеция: " + "Trapeze" + Storage.getListFigures().get(i).toString());
                        //deleteFiguresController.comboBox4.getItems().add("Трапеция: " + "Trapeze" + Storage.getListFigures().get(Storage.getFiguresCount()).toString());
                    }
                    if (figure == "Прямоугольник") {

                        comboBox3.getItems().add("Прямоугольник: " + "Rectangle" + Storage.getListFigures().get(i).toString());
                        //deleteFiguresController.comboBox4.getItems().add("Прямоугольник: " + "Rectangle" + Storage.getListFigures().get(Storage.getFiguresCount()).toString());
                    }
                    break;
            }
        }
    }
    @FXML
    private void comboBox2_SelectedIndexChanged(ActionEvent actionEvent) {
        int selectedIndex = comboBox2.getSelectionModel().getSelectedIndex();
        switch (selectedIndex) {
            case 0:
                pn111.setDisable(false);
                pn222.setDisable(true);
                pn333.setDisable(true);
                break;
            case 1:
                pn111.setDisable(true);
                pn222.setDisable(false);
                pn333.setDisable(true);
                break;
            case 2:
                pn111.setDisable(true);
                pn222.setDisable(true);
                pn333.setDisable(false);
                break;
        }
    }

    @FXML
    private void button5_Click(ActionEvent actionEvent) throws NullInputException {
        if(Storage.getFiguresCount() == 0){
            deleteFiguresController.comboBox4.getSelectionModel().clearSelection();
        }
        else if(deleteFiguresController.comboBox4.getSelectionModel().getSelectedIndex() < 0){
            deleteFiguresController.comboBox4.getSelectionModel().select(0);
        }
        try {
            if (comboBox3.getSelectionModel().getSelectedIndex() == -1 || comboBox2.getSelectionModel().getSelectedIndex() == -1 || (comboBox2.getSelectionModel().getSelectedIndex() == -1 && Storage.getFiguresCount() == 0)) {
                throw new NullInputException();
            } else {
                if (comboBox2.getSelectionModel().getSelectedIndex() == 0 && (textBox38.getText().isEmpty() || textBox39.getText().isEmpty())) {
                    throw new NullInputException();
                }
                if (comboBox2.getSelectionModel().getSelectedIndex() == 1 && textBox40.getText().isEmpty()) {
                    throw new NullInputException();
                }
                if (comboBox2.getSelectionModel().getSelectedIndex() == 2 && domainUpDown1.getValue() == null) {
                    throw new NullInputException();
                }
            }
            String move = comboBox2.getSelectionModel().getSelectedItem();
            String type;
            String originalString;
            String newString;
            switch (move) {
                case "Поворот":
                    if (comboBox3.getSelectionModel().getSelectedIndex() < 0) {
                        comboBox3.getSelectionModel().select(0);
                    }
                    if (deleteFiguresController.comboBox4.getSelectionModel().getSelectedIndex() < 0) {
                        deleteFiguresController.comboBox4.getSelectionModel().select(0);
                    }
                    if (crossFiguresController.comboBox5.getSelectionModel().getSelectedIndex() < 0) {
                        crossFiguresController.comboBox5.getSelectionModel().select(0);
                    }
                    if (crossFiguresController.comboBox6.getSelectionModel().getSelectedIndex() < 0) {
                        crossFiguresController.comboBox6.getSelectionModel().select(0);
                    }
                    Storage.getListFigures().add(Storage.getListFigures().get(comboBox3.getSelectionModel().getSelectedIndex()).rot(Double.parseDouble(textBox40.getText())));
                    Storage.getListFigures().remove(comboBox3.getSelectionModel().getSelectedIndex());
                    comboBox3.getItems().remove(comboBox3.getSelectionModel().getSelectedIndex());
                    type = Storage.getListFigures().get(Storage.getListFigures().size() - 1).getClass().getSimpleName();
                    originalString = Storage.getListFigures().get(Storage.getListFigures().size() - 1).toString();
                    newString = originalString.replace("FiguresFX.", "");
                    type = type.replace("FiguresFX.", "");
                    if ("Circle".equals(type)) {
                        comboBox3.getItems().add("Окружность: " + type + newString);
                    } else if ("NGon".equals(type)) {
                        comboBox3.getItems().add("Многоугольник: " + type + newString);
                    } else if ("Trapeze".equals(type)) {
                        comboBox3.getItems().add("Трапеция: " + type + newString);
                    } else if ("Rectangle".equals(type)) {
                        comboBox3.getItems().add("Прямоугольник: " + type + newString);
                    } else if ("TGon".equals(type)) {
                        comboBox3.getItems().add("Треугольник: " + type + newString);
                    } else if ("Polyline".equals(type)) {
                        comboBox3.getItems().add("Ломанная: " + type + newString);
                    } else if ("QGon".equals(type)) {
                        comboBox3.getItems().add("Четырёхугольник: " + type + newString);
                    } else if ("Segment".equals(type)) {
                        comboBox3.getItems().add("Отрезок: " + type + newString);
                    }
                    break;
                case "Симметрия":
                    String value = domainUpDown1.getValue();
                    if (Objects.equals(value, "x")) {
                        if (comboBox3.getSelectionModel().getSelectedIndex() < 0) {
                            comboBox3.getSelectionModel().select(0);
                        }
                        if (deleteFiguresController.comboBox4.getSelectionModel().getSelectedIndex() < 0) {
                            deleteFiguresController.comboBox4.getSelectionModel().select(0);
                        }
                        if (crossFiguresController.comboBox5.getSelectionModel().getSelectedIndex() < 0) {
                            crossFiguresController.comboBox5.getSelectionModel().select(0);
                        }
                        if (crossFiguresController.comboBox6.getSelectionModel().getSelectedIndex() < 0) {
                            crossFiguresController.comboBox6.getSelectionModel().select(0);
                        }
                        Storage.getListFigures().add(Storage.getListFigures().get(comboBox3.getSelectionModel().getSelectedIndex()).symAxis(0));
                        Storage.getListFigures().remove(comboBox3.getSelectionModel().getSelectedIndex());
                        comboBox3.getItems().remove(comboBox3.getSelectionModel().getSelectedIndex());
                        type = Storage.getListFigures().get(Storage.getListFigures().size() - 1).getClass().getSimpleName();
                        originalString = Storage.getListFigures().get(Storage.getListFigures().size() - 1).toString();
                        newString = originalString.replace("FiguresFX.", "");
                        type = type.replace("FiguresFX.", "");
                        if ("Circle".equals(type)) {
                            comboBox3.getItems().add("Окружность: " + type + newString);
                        } else if ("NGon".equals(type)) {
                            comboBox3.getItems().add("Многоугольник: " + type + newString);
                        } else if ("Trapeze".equals(type)) {
                            comboBox3.getItems().add("Трапеция: " + type + newString);
                        } else if ("Rectangle".equals(type)) {
                            comboBox3.getItems().add("Прямоугольник: " + type + newString);
                        } else if ("TGon".equals(type)) {
                            comboBox3.getItems().add("Треугольник: " + type + newString);
                        } else if ("Polyline".equals(type)) {
                            comboBox3.getItems().add("Ломанная: " + type + newString);
                        } else if ("QGon".equals(type)) {
                            comboBox3.getItems().add("Четырёхугольник: " + type + newString);
                        } else if ("Segment".equals(type)) {
                            comboBox3.getItems().add("Отрезок: " + type + newString);
                        }
                    } else if (Objects.equals(value, "y")) {
                        if (comboBox3.getSelectionModel().getSelectedIndex() < 0) {
                            comboBox3.getSelectionModel().select(0);
                        }
                        if (deleteFiguresController.comboBox4.getSelectionModel().getSelectedIndex() < 0) {
                            deleteFiguresController.comboBox4.getSelectionModel().select(0);
                        }
                        if (crossFiguresController.comboBox5.getSelectionModel().getSelectedIndex() < 0) {
                            crossFiguresController.comboBox5.getSelectionModel().select(0);
                        }
                        if (crossFiguresController.comboBox6.getSelectionModel().getSelectedIndex() < 0) {
                            crossFiguresController.comboBox6.getSelectionModel().select(0);
                        }
                        Storage.getListFigures().add(Storage.getListFigures().get(comboBox3.getSelectionModel().getSelectedIndex()).symAxis(1));
                        Storage.getListFigures().remove(comboBox3.getSelectionModel().getSelectedIndex());
                        comboBox3.getItems().remove(comboBox3.getSelectionModel().getSelectedIndex());
                        type = Storage.getListFigures().get(Storage.getListFigures().size() - 1).getClass().getSimpleName();
                        originalString = Storage.getListFigures().get(Storage.getListFigures().size() - 1).toString();
                        newString = originalString.replace("FiguresFX.", "");
                        type = type.replace("FiguresFX.", "");
                        if ("Circle".equals(type)) {
                            comboBox3.getItems().add("Окружность: " + type + newString);
                        } else if ("NGon".equals(type)) {
                            comboBox3.getItems().add("Многоугольник: " + type + newString);
                        } else if ("Trapeze".equals(type)) {
                            comboBox3.getItems().add("Трапеция: " + type + newString);
                        } else if ("Rectangle".equals(type)) {
                            comboBox3.getItems().add("Прямоугольник: " + type + newString);
                        } else if ("TGon".equals(type)) {
                            comboBox3.getItems().add("Треугольник: " + type + newString);
                        } else if ("Polyline".equals(type)) {
                            comboBox3.getItems().add("Ломанная: " + type + newString);
                        } else if ("QGon".equals(type)) {
                            comboBox3.getItems().add("Четырёхугольник: " + type + newString);
                        } else if ("Segment".equals(type)) {
                            comboBox3.getItems().add("Отрезок: " + type + newString);
                        }
                    } else if (Objects.equals(value, "z")) {
                        if (comboBox3.getSelectionModel().getSelectedIndex() < 0) {
                            comboBox3.getSelectionModel().select(0);
                        }
                        if (deleteFiguresController.comboBox4.getSelectionModel().getSelectedIndex() < 0) {
                            deleteFiguresController.comboBox4.getSelectionModel().select(0);
                        }
                        if (crossFiguresController.comboBox5.getSelectionModel().getSelectedIndex() < 0) {
                            crossFiguresController.comboBox5.getSelectionModel().select(0);
                        }
                        if (crossFiguresController.comboBox6.getSelectionModel().getSelectedIndex() < 0) {
                            crossFiguresController.comboBox6.getSelectionModel().select(0);
                        }
                        Storage.getListFigures().add(Storage.getListFigures().get(comboBox3.getSelectionModel().getSelectedIndex()).symAxis(2));
                        Storage.getListFigures().remove(comboBox3.getSelectionModel().getSelectedIndex());
                        comboBox3.getItems().remove(comboBox3.getSelectionModel().getSelectedIndex());
                        type = Storage.getListFigures().get(Storage.getListFigures().size() - 1).getClass().getSimpleName();
                        originalString = Storage.getListFigures().get(Storage.getListFigures().size() - 1).toString();
                        newString = originalString.replace("FiguresFX.", "");
                        type = type.replace("FiguresFX.", "");
                        if ("Circle".equals(type)) {
                            comboBox3.getItems().add("Окружность: " + type + newString);
                        } else if ("NGon".equals(type)) {
                            comboBox3.getItems().add("Многоугольник: " + type + newString);
                        } else if ("Trapeze".equals(type)) {
                            comboBox3.getItems().add("Трапеция: " + type + newString);
                        } else if ("Rectangle".equals(type)) {
                            comboBox3.getItems().add("Прямоугольник: " + type + newString);
                        } else if ("TGon".equals(type)) {
                            comboBox3.getItems().add("Треугольник: " + type + newString);
                        } else if ("Polyline".equals(type)) {
                            comboBox3.getItems().add("Ломанная: " + type + newString);
                        } else if ("QGon".equals(type)) {
                            comboBox3.getItems().add("Четырёхугольник: " + type + newString);
                        } else if ("Segment".equals(type)) {
                            comboBox3.getItems().add("Отрезок: " + type + newString);
                        }
                    }
                    break;
                case "Сдвиг":
                    if (comboBox3.getSelectionModel().getSelectedIndex() < 0) {
                        comboBox3.getSelectionModel().select(0);
                    }
                    if (deleteFiguresController.comboBox4.getSelectionModel().getSelectedIndex() < 0) {
                        deleteFiguresController.comboBox4.getSelectionModel().select(0);
                    }
                    if (crossFiguresController.comboBox5.getSelectionModel().getSelectedIndex() < 0) {
                        crossFiguresController.comboBox5.getSelectionModel().select(0);
                    }
                    if (crossFiguresController.comboBox6.getSelectionModel().getSelectedIndex() < 0) {
                        crossFiguresController.comboBox6.getSelectionModel().select(0);
                    }
                    Storage.getListFigures().add(Storage.getListFigures().get(comboBox3.getSelectionModel().getSelectedIndex()).shift(new Point2D(new double[]{Double.parseDouble(textBox38.getText()), Double.parseDouble(textBox39.getText())})));
                    Storage.getListFigures().remove(comboBox3.getSelectionModel().getSelectedIndex());
                    comboBox3.getItems().remove(comboBox3.getSelectionModel().getSelectedIndex());
                    type = Storage.getListFigures().get(Storage.getListFigures().size() - 1).getClass().getSimpleName();
                    originalString = Storage.getListFigures().get(Storage.getListFigures().size() - 1).toString();
                    newString = originalString.replace("FiguresFX.", "");
                    type = type.replace("FiguresFX.", "");
                    if ("Circle".equals(type)) {
                        comboBox3.getItems().add("Окружность: " + type + newString);
                    } else if ("NGon".equals(type)) {
                        comboBox3.getItems().add("Многоугольник: " + type + newString);
                    } else if ("Trapeze".equals(type)) {
                        comboBox3.getItems().add("Трапеция: " + type + newString);
                    } else if ("Rectangle".equals(type)) {
                        comboBox3.getItems().add("Прямоугольник: " + type + newString);
                    } else if ("TGon".equals(type)) {
                        comboBox3.getItems().add("Треугольник: " + type + newString);
                    } else if ("Polyline".equals(type)) {
                        comboBox3.getItems().add("Ломанная: " + type + newString);
                    } else if ("QGon".equals(type)) {
                        comboBox3.getItems().add("Четырёхугольник: " + type + newString);
                    } else if ("Segment".equals(type)) {
                        comboBox3.getItems().add("Отрезок: " + type + newString);
                    }
                    break;
            }
            Storage.nameFigures.clear();
            for(int i = 0; i < Storage.figuresCount; i++ )
            {
                type = Storage.getListFigures().get(i).getClass().getSimpleName();
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
            for(int i = 0; i < Storage.getListFigures().size(); i++)
            {
                mainController.draw(Storage.getListFigures().get(i), Color.BLACK);
            }
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Успех");
            alert.setHeaderText(null);
            alert.setContentText("Фигура успешно перемещена");

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
