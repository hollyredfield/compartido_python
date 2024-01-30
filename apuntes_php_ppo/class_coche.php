<?php

class coche{

    private $color;
    private $modelo;

    public function __construct($color, $modelo){
        $this->color = $color;
        $this->modelo = $modelo;
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

}





?>