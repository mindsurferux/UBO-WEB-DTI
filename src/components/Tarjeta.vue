<template>
    <div class="tarjeta">
      <slot />
    </div>
  </template>
  
  <script>
  export default {
    name: "Tarjeta",
  };
  </script>
  
  <style scoped lang="scss">
  .tarjeta {
    background-color: rgb(238, 235, 235);
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    padding: 1rem;
  
    &:hover {
      transform: translateY(-10px);
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
  }
  </style>
  