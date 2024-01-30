<?php

class coche2{

    private $color;
    private $modelo;

    public function __construct(){
        //constructor vacío
    }

    public function get_color(){
        return $this->color;
    }

    public function get_modelo(){
        return $this->modelo;
    }
    
    public function set_color($color){
        $this->color = $color;
    }

    public function set_modelo($modelo){
        $this->modelo = $modelo;
    }

    public function ver_atributos(){
        echo "Color: ". $this->color.PHP_EOL;
        echo "Modelo: ". $this->modelo.PHP_EOL;
    }

}





?>