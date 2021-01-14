import numpy as np

pruning_kernels = [
    np.array([[0,-1,-1],
             [1, 1,-1],
             [0,-1,-1]], dtype=np.int),

    np.array([[ 0, 1, 0],
             [-1, 1,-1],
             [-1,-1,-1]], dtype=np.int),

    np.array([[-1,-1, 0],
             [-1, 1, 1],
             [-1,-1, 0]], dtype=np.int),

    np.array([[-1,-1,-1],
             [-1, 1,-1],
             [ 0, 1, 0]], dtype=np.int),

    np.array([[ 1,-1,-1],
             [-1, 1,-1],
             [-1,-1,-1]], dtype=np.int),

    np.array([[-1,-1, 1],
             [-1, 1,-1],
             [-1,-1,-1]], dtype=np.int),

    np.array([[-1,-1,-1],
             [-1, 1,-1],
             [-1,-1, 1]], dtype=np.int),

    np.array([[-1,-1,-1],
             [-1, 1,-1],
             [ 1,-1,-1]], dtype=np.int)]

thinning_kernels = [
    np.array([[-1,-1,-1],
             [-1, 1,-1],
             [ 1, 1, 1]], dtype=np.int),

    np.array([[-1,-1,-1],
             [ 1, 1,-1],
             [-1, 1,-1]], dtype=np.int),

    np.array([[ 1,-1,-1],
              [ 1, 1,-1],
              [ 1,-1,-1]], dtype=np.int),

    np.array([[-1, 1,-1],
              [ 1, 1,-1],
              [-1,-1,-1]], dtype=np.int),

    np.array([[ 1, 1, 1],
              [-1, 1,-1],
              [-1,-1,-1]], dtype=np.int),

    np.array([[-1, 1, -1],
              [-1, 1, 1],
              [-1,-1,-1]], dtype=np.int),

    np.array([[-1,-1, 1],
              [-1, 1, 1],
              [-1,-1, 1]], dtype=np.int),

    np.array([[-1,-1,-1],
              [-1, 1, 1],
              [-1, 1,-1]], dtype=np.int)]

thinning_kernels_w = [
    np.array([[-1,-1,-1],
              [ 0, 1, 0],
              [ 1, 1, 1]], dtype=np.int),

    np.array([[-1, 0, 1],
              [-1, 1, 1],
              [-1, 0, 1]], dtype=np.int),

    np.array([[ 1, 1, 1],
              [ 0, 1, 0],
              [ 1,-1,-1]], dtype=np.int),

    np.array([[ 1, 0,-1],
              [ 1, 1,-1],
              [ 1, 0,-1]], dtype=np.int),

    np.array([[ 0,-1,-1],
              [ 1, 1,-1],
              [ 0, 1, 0]], dtype=np.int),

    np.array([[-1,-1, 0],
              [-1, 1, 1],
              [ 0, 1, 0]], dtype=np.int),

    np.array([[ 0, 1, 0],
              [-1, 1, 1],
              [-1,-1, 0]], dtype=np.int),

    np.array([[ 0, 1, 0],
              [ 1, 1,-1],
              [ 0,-1,-1]], dtype=np.int),

    np.array([[ 1, 0,-1],
              [ 0, 1,-1],
              [-1,-1,-1]], dtype=np.int),
        
    np.array([[-1, 0, 1],
              [-1, 1, 0],
              [-1,-1,-1]], dtype=np.int),
    
    np.array([[-1,-1,-1],
              [-1, 1, 0],
              [-1, 0, 1]], dtype=np.int),
    
    np.array([[-1,-1,-1],
              [ 0, 1,-1],
              [ 1, 0,-1]], dtype=np.int)]

ridge_terminations_kernel = [
    np.array([[-1, 1,-1],
              [-1, 1,-1],
              [-1,-1,-1]], dtype=np.int),

    np.array([[-1,-1,-1],
              [-1, 1, 1],
              [-1,-1,-1]], dtype=np.int),

    np.array([[-1,-1,-1],
              [-1, 1,-1],
              [-1, 1,-1]], dtype=np.int),
    
    np.array([[-1,-1,-1],
              [ 1, 1,-1],
              [-1,-1,-1]], dtype=np.int),
    
    np.array([[ 1,-1,-1],
              [-1, 1,-1],
              [-1,-1,-1]], dtype=np.int),
        
    np.array([[-1,-1, 1],
              [-1, 1,-1],
              [-1,-1,-1]], dtype=np.int),
    
    np.array([[-1,-1,-1],
              [-1, 1,-1],
              [-1,-1, 1]], dtype=np.int),
    
    np.array([[-1,-1,-1],
              [-1, 1,-1],
              [ 1,-1,-1]], dtype=np.int)]

ridge_bifurcations_kernel = [
    np.array([[-1,-1, 1],
              [ 1, 1,-1],
              [-1,-1, 1]], dtype=np.int),

    np.array([[-1, 1,-1],
              [-1, 1,-1],
              [ 1,-1, 1]], dtype=np.int),

    np.array([[ 1,-1,-1],
              [-1, 1, 1],
              [ 1,-1,-1]], dtype=np.int),
    
    np.array([[ 1,-1, 1],
              [-1, 1,-1],
              [-1, 1,-1]], dtype=np.int),
    
    np.array([[-1, 1,-1],
              [-1, 1, 1],
              [ 1,-1,-1]], dtype=np.int),
        
    np.array([[ 1,-1,-1],
              [-1, 1, 1],
              [-1, 1,-1]], dtype=np.int),
    
    np.array([[-1,-1, 1],
              [ 1, 1,-1],
              [-1, 1,-1]], dtype=np.int),
    
    np.array([[-1, 1,-1],
              [ 1, 1,-1],
              [-1,-1, 1]], dtype=np.int)]